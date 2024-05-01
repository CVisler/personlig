from pydantic import field_validator, BaseModel, Field, computed_field
from enum import StrEnum, member
from typing import Optional, List, TypedDict


class SnordTables(StrEnum):
    ACTUALS = 'actuals'
    SST = 'sst'


class Period(str):
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
    period: list[str] # Why is this a list of strings? Because the sony_calendar() is set up to return strings I believe
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
    table: SnordTables
    period: Optional[int | list[int]] = Field(default=None,
                                            ge=201001,
                                            le=202653,
                                            title="Periods to include")

    class Config:
        extra = 'forbid'
        validate_assignment = True


    @field_validator('table')
    def validate_table(cls, v):
        if v not in SQL_META_DATA:
            raise ValueError(f"Table {v} not found in SQL_META_DATA")
        return v


    @computed_field
    @property
    def period_type(self) -> Period.Type:
        return SQL_META_DATA[self.table]['period_type']


    @field_validator('period')
    def validate_period(cls, v):
        __v = str(v)
        if int(__v[-2:]) not in range(1, 54):
            raise ValueError(f"Period {v} not found in SQL_META_DATA")
        return v


print(
    Model(
        table='sst',
        period='202453'
    ).dict()
)
