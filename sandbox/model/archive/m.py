from pydantic import (
    BaseModel,
    Field,
    field_validator,
    ConfigDict,
    computed_field,
)
from model_validators import month_, week_, month_dot, week_dot
from metadata import SQL_META_DATA as META
from enums import Period, SnordTable
from typing import List, Any, Sequence

from sony import calyear_fiscyear as _conv, dotyear as _dot



class Init(BaseModel):
    model_config = ConfigDict(use_enum_values=True)


    table: SnordTable | str = Field(...,)
    period: List[month_ | week_ | None] | None = None
    period_type: Period.Type | None = None
    period_def: Period.Def | None = None
    period_sap: Period.Sap | None = None
    period_tech_name: List[str] | None = None
    new_cols: List[str] | None = None



    @field_validator('period', mode='before')
    @classmethod
    def check_list(cls, v):
        if not isinstance(v, list):
            return [v]
        else:
            return v



    def model_post_init(self, __context: Any) -> None:
        if not self.period:
            self.period = META[self.table]['period']
        self.period_type = META[self.table]['period_type']
        self.period_def = META[self.table]['period_def']
        self.period_sap = META[self.table]['period_sap']
        self.period_tech_name = META[self.table]['period_tech_name']
        self.new_cols = META[self.table]['new_cols']



class Construct(Init):
    @computed_field
    @property
    def period_sap_entry(self) -> Sequence[month_ | week_ | month_dot | week_dot]:
        if self.period_type != Period.Type.year_week:
            if self.period_def == Period.Def.fiscal:
                return _conv(self.period)
            else:
                return self.period 
        else:
            return self.period



    @computed_field
    @property
    def period_sap_entry_final(self) -> str | Sequence[month_dot | week_dot]:
        period_sap_entry_final_ = [str(i) for i in self.period_sap_entry]


        if self.period_sap == Period.Sap.interval:
            if len(period_sap_entry_final_) > 1:
                period_sap_entry_final_ = ' - '.join(
                    [period_sap_entry_final_[0],
                    period_sap_entry_final_[-1]]
                )
            else:
                period_sap_entry_final_ = period_sap_entry_final_[0]


        if self.period_sap == Period.Sap.dot_interval:
            if len(period_sap_entry_final_) > 1:
                period_sap_entry_final_ = ' - '.join(
                    [
                        _dot(period_sap_entry_final_[0])[0], # _dot() returns a list, hence the [0] to perform .join()
                        _dot(period_sap_entry_final_[-1])[0]
                    ]
                )
            else:
                period_sap_entry_final_ = _dot(period_sap_entry_final_[0])[0]


        if self.period_sap == Period.Sap.dot_full:
            period_sap_entry_final_ = _dot(
                period_sap_entry_final_
            )


        return period_sap_entry_final_
