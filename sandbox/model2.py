from pydantic import field_validator, BaseModel, Field, ValidationError, model_validator, AfterValidator
from enum import StrEnum, member
from typing import Optional, List, TypedDict
from typing_extensions import Annotated


class SnordTables(StrEnum):
    ACTUALS = 'actuals'
    SST = 'sst'


class Period:
    class Type(StrEnum):
        year_month = 'year_month'
        year_week = 'year_week'
    class Def(StrEnum):
        fiscal = 'fiscal'
        calendar = 'calendar'
    class Sap(StrEnum):
        interval = 'interval'
        full = 'full'
        dot_interval = 'dot_interval'
        dot_full = 'dot_full'


class SQLTableContent(TypedDict):
    alias: list[str]
    period: list[str]
    period_type: Period.Type
    period_def: Period.Def
    period_sap: Period.Sap
    period_tech_name: list[str]
    new_cols: list[str]


class SQLMetaData(TypedDict):
    SnordTables.ACTUALS: SQLTableContent
    SnordTables.SST: SQLTableContent


SQL_META_DATA: SQLMetaData = {
    SnordTables.ACTUALS: {
        'alias': [ 'DS_1' ],
        'period': ['202402', '202403', '202404'],
        'period_type': Period.Type.year_month,
        'period_def': Period.Def.calendar,
        'period_sap': Period.Sap.full,
        'period_tech_name': ['S_FYPOPT'],
        'new_cols': ['DATE', 'CUSTOMER', 'MATERIAL', 'QUANTITY', 'P3B_1', 'P3B', 'P5', 'MP'],
    },
    SnordTables.SST: {
        'alias': [ 'DS_3' ],
        'period': ['202422', '202423', '202424'],
        'period_type': Period.Type.year_week,
        'period_def': Period.Def.calendar,
        'period_sap': Period.Sap.full,
        'period_tech_name': ['S_CALWK_MS'],
        'new_cols': ['DATE', 'CUSTOMER', 'EXT_ID', 'MATERIAL', 'SELLOUT', 'STOCK'],
    },
}


class Model(BaseModel):
    table: SnordTables = Field(..., title="Table name", description="Assigns all the table's attributes based off table name")
    period_type: Optional[Period.Type] = Period.Type.year_month
    period: Optional[int | list[int]] = 0
    class Config:
        extra = 'forbid'
        validate_assignment = True


    # Override the initializor to set the period type
    def __init__(self, **data):
        super().__init__(**data)
        self.period_type = SQL_META_DATA[self.table]['period_type']
        self.period = SQL_META_DATA[self.table]['period'] if self.period == 0 else self.period


    @model_validator(mode='after')
    def validate_period(self):
        if isinstance(self.period, list):
            for p in self.period:
                s = str(p)
                if len(s) != 6:
                    raise ValueError(f"{s} must be six digits long, got {len(s)}")
                if int(s[:4]) not in range(2010, 2031):
                    raise ValueError(f"{self.period_type} is not an acceptable year")
                if self.period_type == Period.Type.year_month:
                    if int(s[-2:]) not in range(1, 13):
                        raise ValueError(f"{self.period_type} is not an acceptable month interval")
                elif self.period_type == Period.Type.year_week:
                    if int(s[-2:]) not in range(1, 54):
                        raise ValueError(f"{self.period_type} is not an acceptable week interval")
                return self

        else:
            s = str(self.period)
            if len(s) != 6:
                raise ValueError(f"{s} must be six digits long, got {len(s)}")
            if int(s[:4]) not in range(2010, 2031):
                raise ValueError(f"{self.period_type} is not an acceptable year")
            if self.period_type == Period.Type.year_month:
                if int(s[-2:]) not in range(1, 13):
                    raise ValueError(f"{self.period_type} is not an acceptable month interval")
            elif self.period_type == Period.Type.year_week:
                if int(s[-2:]) not in range(1, 54):
                    raise ValueError(f"{self.period_type} is not an acceptable week interval")
            return self


# TODO: Default value is a list but is not recognized as such by the inner validator
if __name__ == '__main__':
    try:
        print(
            Model(
                table='actuals',
                # period=['202411', '202310', '202202']
            ).model_dump_json(indent=2)
        )
    except ValidationError as e:
        print(e.json(indent=2))
