from pydantic import (
    field_validator,
    BaseModel,
    Field,
    ValidationError,
    ConfigDict,
)
from model_validators import month_, week_
from metadata import SQL_META_DATA as META
from enums import Period
from typing import List, Any, Literal

import sony as s
from sony import calyear_fiscyear as _conv, dotyear as _dot, sony_calendar as sc


class Vp(BaseModel):
    month: List[month_] = Field(
        kw_only=True,
        max_length=12, # Max list length
        examples=[202403, 202404],
        default_factory=list,)


    week: List[week_] = Field(
        kw_only=True,
        max_length=3, # Max list length
        examples=[202333, 202334],
        default_factory=list,)


    @field_validator('month', 'week', mode='before')
    @classmethod
    def check_list(cls, v):
        if not isinstance(v, list):
            return [v]
        else:
            return v


class Inst(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    table: str = Field(...,
                              examples=['actuals', 'sst'],)
    period: List[month_ | week_] | None = None
    period_type: Period.Type | None = None
    period_def: Period.Def | None = None
    period_sap: Period.Sap | None = None
    period_tech_name: List[str] | None = None
    new_cols: List[str] | None = None


    def model_post_init(self, __context: Any) -> None:
        if not self.period:
            self.period = META[self.table]['period']
        self.period_type = META[self.table]['period_type']
        self.period_def = META[self.table]['period_def']
        self.period_sap = META[self.table]['period_sap']
        self.period_tech_name = META[self.table]['period_tech_name']
        self.new_cols = META[self.table]['new_cols']


# if __name__ == "__main__":
#     try:
#         prd = Vp(
#             month=[ 202202 ],
#         )
#
#         model = Inst(
#             table='actuals',
#             period=prd.month,
#         )
#
#         print( model.model_dump_json(indent=2))
#     except ValidationError as e:
#         print(e.json(indent=2))
