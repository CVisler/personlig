from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
    ConfigDict,
    ValidationInfo,
    ValidationError,
)
from model_validators import month_, week_, month_dot, week_dot
from metadata import SQL_META_DATA as META
from enums import Period, SnordTable
from typing import List, Any, Sequence, Annotated

# from sony import calyear_fiscyear as _conv, dotyear as _dot


class Init(BaseModel):
    # model_config = ConfigDict(use_enum_values=True, validate_default=True)

    table: SnordTable | str
    period: List[month_ | week_ | None] | None = None
    period_type: Period.Type | None = None
    period_def: Period.Def | None = None
    period_sap: Period.Sap | None = None
    period_tech_name: List[str] | None = None
    new_cols: List[str] | None = None


    @field_validator('period')
    @classmethod
    def set_period(cls, v: month_ | week_, info: ValidationInfo) -> month_ | week_:
        table_ = info.data.get('table')
        if v is None:
            return META.get(table_).get('period')
        else:
            return v


    @model_validator(mode='before')
    @classmethod
    def check_period_type(cls, data: Any) -> Any:
        if isinstance(data, dict):
            if 'table' in data:
                data['new_cols'] = ['test']
                return data



    # @field_validator('period_type', 'period_def', 'period_sap', 'period_tech_name', 'new_cols')
    # @classmethod
    # def set_period_type(cls, v: Any, info: ValidationInfo) -> Any:
    #     table_ = info.data.get('table')
        # info.data['new_cols'] = Period.Type.year_month



    # @field_validator('period_def')
    # @classmethod
    # def set_period_def(cls, v: Period.Def, info: ValidationInfo) -> Period.Def:
    #     table_ = info.data.get('table')
    #     if v:
    #         raise ValueError('Period.Def could not be determined from the SQL_META_DATA dictionary')
    #     return META.get(table_).get('period_def')



class Construct(Init):
    pass


if __name__ == '__main__':
    try:
        print(Init(table='actuals'))
    except ValidationError as e:
        print(e)
    # print(Init.model_validate(Init.construct()))
    # print(
    #     Init(
    #         table='actuals',
    #         # period=202010,
    #     ).model_dump_json(indent=2)
    # )
