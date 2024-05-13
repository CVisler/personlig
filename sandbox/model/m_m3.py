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
from model_validators import month_, week_, month_dot, week_dot
from metadata import SQL_META_DATA as META
from enums import Period, SnordTable
from typing import List, Any, Sequence, Annotated

# from sony import calyear_fiscyear as _conv, dotyear as _dot


class Init(BaseModel):
    """
    Initializes the model with the necessary parameters for the SQL query.
    Only required field is the table name. Period can optionally be passed as a list of integers - model will attempt to coerce if anything else is passed.

    """
    model_config = ConfigDict(use_enum_values=True, validate_default=True)

    table: SnordTable | str
    period: Annotated[List[month_ | week_], BeforeValidator(lambda v: [v] if not isinstance(v, list) else v)] = [202403, 202404, 202405] # Convert user input to list if it isnt alread
    period_type: Period.Type | None = None
    period_def: Period.Def | None = None
    period_sap: Period.Sap | None = None
    period_tech_name: List[str] | None = None
    new_cols: List[str] | None = None


    #TODO: Field validator for period before inner validation takes place which should assign period from META dict


    @model_validator(mode='before')
    @classmethod
    def populate_meta_model(cls, data: Any) -> Any:
        if isinstance(data, dict):
            # TODO: Currently hard coded for testing
            data['period_type'] = Period.Type.year_month
            data['period_def'] = Period.Def.calendar
            data['period_sap'] = Period.Sap.dot_interval
            data['period_tech_name'] = ['S_FYPOPT']
            data['new_cols'] = ['DATE', 'CUSTOMER', 'MATERIAL', 'QUANTITY', 'P3B_1', 'P3B', 'P5', 'MP']
            return data



class Construct(Init):
    pass


if __name__ == '__main__':
    try:
        print(
            Init(
                table='actuals',
                # period=202010,
            ).model_dump_json(indent=2)
        )
        # print(Init(table='actuals'))
    except ValidationError as e:
        print(e.json(indent=2))
