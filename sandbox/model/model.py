from pydantic import (
    field_validator,
    computed_field,
    model_validator,
    BaseModel,
    Field,
    ValidationError,
    AfterValidator,
)
from validators import test_month, test_week, month_, week_
from metadata import SQL_META_DATA as META
from enums import SnordTable, Period
from typing import List


class ValidatedPeriod(BaseModel):
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
    table: SnordTable = Field(...,
                              examples=['actuals', 'sst'],)
    period: List[month_ | week_] | None = None
    period_type: Period.Type | None = None
    period_def: Period.Def | None = None
    period_sap: Period.Sap | None = None
    period_tech_name: List[str] | None = None
    new_cols: List[str] | None = None


    def model_post_init(self, __context: any) -> None:
        if not self.period:
            self.period = META[self.table.value]['period']
        self.period_type = META[self.table.value]['period_type']
        self.period_def = META[self.table.value]['period_def']
        self.period_sap = META[self.table.value]['period_sap']
        self.period_tech_name = META[self.table.value]['period_tech_name']
        self.new_cols = META[self.table.value]['new_cols']


if __name__ == "__main__":
    try:
        prd = ValidatedPeriod(
            month=202202,
        )

        model = Inst(
            table='actuals',
            period=prd.month,
        )

        print( model.model_dump_json(indent=2))
    except ValidationError as e:
        print(e.json(indent=2))
