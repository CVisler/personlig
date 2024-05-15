from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
    ConfigDict,
    ValidationInfo,
    BeforeValidator,
)
import datetime
# from xlwings import Book

from model_validators import (
    month_, week_,
    month_dot, week_dot,
    test_month, test_week,
)
from sony import calyear_fiscyear as _conv, dotyear as _dot, calyear_date as _date, sonyyearweek_date as _week_to_date
from metadata import SQL_META_DATA as META
from enums import Period, SnordTable
from typing import Dict, List, Any, Annotated, TypeAlias
period_: TypeAlias = List[month_ | week_ | month_dot | week_dot]
period_sap_: TypeAlias = str | List[str]
_period_ = Annotated[List[month_ | week_], BeforeValidator(lambda v: [v] if not isinstance(v, list) else v)]



class Init(BaseModel):
    """
    Initializes the model with the necessary parameters for the SQL query.
    Only required field is the table name. Period can optionally be passed as a list of integers - model will attempt to coerce if anything else is passed.

    """
    model_config = ConfigDict(use_enum_values=True, validate_default=True)

    table: SnordTable | str = Field(..., description='Table name')
    alias: str | None = Field(default=None, exclude=True, repr=False)
    period_type: Period.Type | None = Field(default=None, exclude=True, repr=False) # Set period type first in order to determine how period should be validated, i.e. month or week
    period: _period_ | None = None
    period_def: Period.Def | None = Field(default=None, exclude=True, repr=False)
    period_sap: Period.Sap | None = Field(default=None, exclude=True, repr=False)
    period_tech_name: List[str] | None = Field(default=None, exclude=True, repr=False)
    new_cols: List[str] | None =  Field(default=None, exclude=True, repr=False)
    technical_name: List[str] | None = Field(default=None, exclude=True, repr=False)


    # FIRST ASSIGN META DATA TO MODEL BEFORE ANY VALIDATION
    # Assign period only if user has provided it
    @model_validator(mode='before')
    @classmethod
    def populate_meta_model(cls, data: Dict) -> Dict:
        if isinstance(data, dict):
            # FIRST OFF ENSURE THAT TABLE NAME IS PROVIDED
            if not data.get('table', None):
                raise ValueError('Table name is required')

            data['alias'] = META[data['table']]['alias']
            prd_type_ = META[data['table']]['period_type']
            data['period_type'] = prd_type_

            if data.get('period', None): # If user has overwridden default period then validate and assign it
                prd_ = data['period']
                if not isinstance(prd_, list): # Coerce to list if not already
                    prd_ = [prd_]
                data['period'] = test_month(prd_) if prd_type_ == Period.Type.year_month else test_week(prd_)

            if prd_type_ == Period.Type.year_week:
                if META[data['table']]['period_def'] != Period.Def.calendar:
                    print(f'Period.Def type not correctly set to calendar for table {data["table"]} which has year_week type. It has been coerced to right type but please review SQL_META_DATA')
                data['period_def'] = Period.Def.calendar
            else:
                data['period_def'] = META[data['table']]['period_def']

            data['period_sap'] = META[data['table']]['period_sap']
            data['period_tech_name'] = META[data['table']]['period_tech_name']
            data['new_cols'] = META[data['table']]['new_cols']
            return data



    # IF NO USER OVERRIDE DEFER TO DEFAULT PERIOD
    @field_validator('period')
    @classmethod
    def assign_period(cls, v: Any, info: ValidationInfo) -> Any: # No validators have run on period attr yet so it could be Any
        return META[info.data['table']]['period'] if not v else v # Default period is validated in metadata.DefaultPeriod()



class Construct(Init):
    model_config = ConfigDict(use_enum_values=True, validate_default=True)

    period_sap_entry: period_sap_ | None = Field(default=None, exclude=True, repr=False) 
    period_iso: List[datetime.date] | None = Field(default=None, exclude=True, repr=False) 



    @field_validator('period_sap_entry', mode='after')
    @classmethod
    def generate_prd_sap_entry(cls, v: None, info: ValidationInfo) -> period_sap_:
        if not info.data.get('period', None):
            raise ValueError('None or invalid period handed to Construct.generate_prd_sap_entry()')

        period_sap_ = info.data['period_sap']
        period_sap_entry_final_ = info.data['period']


        # Determine period type and definition and convert to fiscal period if necessary
        if info.data['period_type'] != Period.Type.year_week:
            if info.data['period_def'] == Period.Def.fiscal:
                period_sap_entry_final_ = _conv(info.data['period'])
            else:
                period_sap_entry_final_ = [str(i) for i in info.data['period']] # Converting to string for below string manipulation
        else:
            period_sap_entry_final_ = [str(i) for i in info.data['period']] # If period is to be interpreted as week take period assigned


        if period_sap_ == Period.Sap.interval:
            if len(period_sap_entry_final_) > 1: # Check whether single input was provided
                period_sap_entry_final_ = ' - '.join(
                    [period_sap_entry_final_[0],
                    period_sap_entry_final_[-1]]
                )
            else:
                period_sap_entry_final_ = period_sap_entry_final_[0]


        if period_sap_ == Period.Sap.dot_interval:
            if len(period_sap_entry_final_) > 1:
                period_sap_entry_final_ = ' - '.join(
                    [
                        _dot(period_sap_entry_final_[0])[0], # _dot() returns a list, hence the [0] to perform .join()
                        _dot(period_sap_entry_final_[-1])[0]
                    ]
                )
            else:
                period_sap_entry_final_ = _dot(period_sap_entry_final_[0])[0]


        if period_sap_ == Period.Sap.dot_full:
            period_sap_entry_final_ = _dot(
                period_sap_entry_final_
            )


        return period_sap_entry_final_



    @field_validator('period_iso', mode='after')
    @classmethod
    def generate_prd_iso(cls, v: Any, info: ValidationInfo) -> List[datetime.date]:
        if not info.data.get('period', None):
            raise ValueError('None or invalid period handed to Construct.generate_prd_sap_entry()')

        if info.data['period_type'] == Period.Type.year_week:
            _ = [_week_to_date(i) for i in info.data['period']]
            return [datetime.datetime.strptime(d, "%Y-%m-%d").date() for d in _]
        else:
            return [datetime.datetime.strptime(d, "%Y-%m-%d").date() for d in _date(info.data['period'])]
