from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
    ConfigDict,
    ValidationInfo,
    ValidationError,
    BeforeValidator,
)
import datetime

from model_validators import (
    month_, week_,
    month_dot, week_dot,
    test_month, test_week,
)
from sony import calyear_fiscyear as _conv, dotyear as _dot, calyear_date as _date
from metadata import SQL_META_DATA as META
from enums import Period, SnordTable
from typing import Dict, List, Any, Sequence, Annotated, TypeAlias
period_: TypeAlias = List[month_ | week_ | month_dot | week_dot]
# _period_: TypeAlias = List[month_ | week_] #, BeforeValidator(lambda v: [v] if not isinstance(v, list) else v)]
_period_ = Annotated[List[month_ | week_], BeforeValidator(lambda v: [v] if not isinstance(v, list) else v)]



class Init(BaseModel):
    """
    Initializes the model with the necessary parameters for the SQL query.
    Only required field is the table name. Period can optionally be passed as a list of integers - model will attempt to coerce if anything else is passed.

    """
    model_config = ConfigDict(use_enum_values=True, validate_default=True)

    table: SnordTable | str
    period_type: Period.Type | None = Field(default=None, exclude=True, repr=False) # Set period type first in order to determine how period should be validated, i.e. month or week
    period: _period_ | None = None
    period_def: Period.Def | None = Field(default=None, exclude=True, repr=False)
    period_sap: Period.Sap | None = Field(default=None, exclude=True, repr=False)
    period_tech_name: List[str] | None = Field(default=None, exclude=True, repr=False)
    new_cols: List[str] | None =  Field(default=None, exclude=True, repr=False)
    technical_name: List[str] | None = Field(default=None, exclude=True, repr=False)


    @model_validator(mode='before')
    @classmethod
    def populate_meta_model(cls, data: Dict) -> Dict:
        if isinstance(data, dict):
            data['period_type'] = META[data['table']]['period_type']
            data['period_def'] = META[data['table']]['period_def']
            data['period_sap'] = META[data['table']]['period_sap']
            data['period_tech_name'] = META[data['table']]['period_tech_name']
            data['new_cols'] = META[data['table']]['new_cols']
            return data



    @field_validator('period', mode='before')
    @classmethod
    def assign_period(cls, v: Any, info: ValidationInfo) -> Any: # No validators have run on period attr yet so it could be Any
        return META[info.data['table']]['period'] if not v else v



    @field_validator('period')
    @classmethod
    def check_period(cls, v: Any, info: ValidationInfo) -> _period_:
        if info.data['period_type'] == Period.Type.year_month:
            return [test_month(i) for i in v]
        elif info.data['period_type'] == Period.Type.year_week:
            return [test_week(i) for i in v]



class Construct(Init):
    model_config = ConfigDict(use_enum_values=True, validate_default=True)

    period_sap_entry: period_ | None = Field(default=None, exclude=True, repr=False) 
    # period_iso: List[datetime.date] | None = Field(default=None, exclude=True, repr=False) 


    @field_validator('period_sap_entry')
    @classmethod
    def generate_prd_sap_entry(cls, v: Any, info: ValidationInfo) -> period_:
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



    # @field_validator('period_iso')
    # @classmethod
    # def generate_prd_iso(cls, v: Any, info: ValidationInfo) -> List[datetime.date]:
    #     return [datetime.datetime.strptime(d, "%Y-%m-%d").date() for d in _date(info.data['period'])]



if __name__ == '__main__':
    try:
        c = Construct(
                table='actuals',
                period=202302, # TODO: Need to handle error in init if non iterable is passed so we can produce proper error
            )

        print(c.model_dump_json(indent=2))
        # print(c)
        # print(c.period_type)

    except ValidationError as e:
        print(e.json(indent=2))
