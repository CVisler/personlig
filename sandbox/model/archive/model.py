from pydantic import (
    field_validator,
    BaseModel,
    Field,
    ValidationError,
    ConfigDict,
)
from model_validators import month_, week_, month_dot, week_dot
from metadata import SQL_META_DATA as META, ValidatedPeriod
from enums import Period
from typing import List, Any, Literal

import sony as s
from sony import calyear_fiscyear as _conv, dotyear as _dot, sony_calendar as sc


class Inst(ValidatedPeriod):
    model_config = ConfigDict(use_enum_values=True)
    table: str = Field(...,
                              examples=['actuals', 'sst'],)
    period: List[month_ | week_] | None = None
    period_sap_entry: List[month_dot | week_dot] | None = None
    period_type: Period.Type | None = None
    period_def: Period.Def | None = None
    period_sap: Period.Sap | None = None
    period_tech_name: List[str] | None = None
    new_cols: List[str] | None = None


    def model_post_init(self, __context: Any) -> None:
        # Mypy complains that I use variables as keys for the TypeDict SQL_META_DATA dict - however it works
        if not self.period:
            self.period = META[self.table]['period']
            self.period_sap_entry = META[self.table]['period_sap_entry']
        else:
            # TODO: Solution; computed_fields ??
            self.period_sap_entry = META[self.table]['period_sap_entry']
        self.period_type = META[self.table]['period_type']
        self.period_def = META[self.table]['period_def']
        self.period_sap = META[self.table]['period_sap']
        self.period_tech_name = META[self.table]['period_tech_name']
        self.new_cols = META[self.table]['new_cols']


if __name__ == "__main__":
    try:
        prd = ValidatedPeriod(
            month=[ 202202 ],
        )

        model = Inst(
            table='actuals',
            period=prd.month,
            # TODO: This is uncool: I now need to know the type of sap entry in order to manually set it
            # period_sap_entry=prd.dot_conv_month,
        )

        print(prd.dot_conv_month)
        print(model.period_sap_entry)
        print(model.period)
        # print( model.model_dump_json(indent=2))
    except ValidationError as e:
        print(e.json(indent=2))
