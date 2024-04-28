from pydantic import field_validator, BaseModel, Field
from pydantic.dataclasses import dataclass
import dataclasses
from enum import StrEnum
from typing import Optional, List

def_ym = ['202312', '202411', 202412, '202301', '202302', '202303', '202304', '202305', '202306', '202307', '202308', '202309', '202310', '202311']

class PeriodDef(StrEnum):
    year_month = 'year_month'
    year_week = 'year_week'

@dataclass(kw_only=True, slots=True)
class PeriodType:
    ym: Optional[List[int]] = Field(examples=[202403, 202404], default=None)
    yw: Optional[List[int]] = Field(examples=[202333, 202334], default=None)

    @field_validator('ym')
    @classmethod
    def test_year_month(cls, v):
        def _test_ix(v):
            __str = str(v)
            if len(__str) != 6:
                raise ValueError(f'{v} has wrong amount of digits ({len(__str)}) and not 6.')
            if __str[:2] != '20':
                raise ValueError(f'{v} is not an acceptable year')
            if __str[2:4] not in [str(i).zfill(2) for i in range(10, 27)]:
                raise ValueError(f'{v} is not an acceptable year')
            if __str[-2:] not in [str(i).zfill(2) for i in range(1, 13)]:
                raise ValueError(f'{__str[-2:]} is not in the acceptable range of months')
            return v
        return [_test_ix(i) for i in v]

    @field_validator('yw')
    @classmethod
    def test_year_week(cls, v):
        def _test_ix(v):
            __str = str(v)
            if len(__str) != 6:
                raise ValueError(f'{v} has wrong amount of digits.')
            if __str[:2] != '20':
                raise ValueError(f'{v} is not an acceptable year')
            if __str[2:4] not in [str(i).zfill(2) for i in range(10, 27)]:
                raise ValueError(f'{v} is not an acceptable year')
            if __str[-2:] not in [str(i).zfill(2) for i in range(1, 54)]:
                raise ValueError(f'{__str[-2:]} is not in the acceptable range of weeks')
            return v
        return [_test_ix(i) for i in v]

class Procedure(BaseModel):
    period_def: PeriodDef = Field(default=None)
    period: PeriodType = Field(default_factory=PeriodType, validate_default=True)


    def model_post_init(self, __context: any) -> None:
        if self.period.ym:
            self.period_def = PeriodDef.year_month
        elif self.period.yw:
            self.period_def = PeriodDef.year_week


procedure = Procedure(
    period_def=PeriodDef.year_month,
    period=PeriodType(
        yw=def_ym,
    )
)
print(procedure.model_dump_json(indent=4))
print(procedure.model_dump())
