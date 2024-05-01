from pydantic import field_validator, BaseModel, Field
from pydantic.dataclasses import dataclass
from enum import StrEnum
from typing import Optional, List, TypedDict


class SnordTables(StrEnum):
    ACTUALS = 'actuals'
    SST = 'sst'


class PeriodType(StrEnum):
    year_month = 'year_month'
    year_week = 'year_week'


class PeriodDef(StrEnum):
    fiscal = 'fiscal'
    calendar = 'calendar'


class PeriodSap(StrEnum):
    interval = 'interval'
    full = 'full'
    dot_interval = 'dot_interval'
    dot_full = 'dot_full'


class SQLTableContent(TypedDict):
    alias: str
    period: list[str] # Why is this a list of strings? Because the sony_calendar() is set up to return strings I believe
    period_type: PeriodType
    period_tech_name: list[str]
    new_cols: list[str]


class SQLMetaData(TypedDict):
    SnordTables.ACTUALS: SQLTableContent
    SnordTables.SST: SQLTableContent


SQL_META_DATA: SQLMetaData = {
    SnordTables.ACTUALS: {
        'alias': 'DS_1',
        'period': ['202402', '202403', '202404'],
        'period_type': PeriodType.year_month,
        'period_def': PeriodDef.calendar,
        'period_sap': PeriodSap.full,
        'period_tech_name': ['S_FYPOPT'],
        'new_cols': ['DATE', 'CUSTOMER', 'MATERIAL', 'QUANTITY', 'P3B_1', 'P3B', 'P5', 'MP'],
    },
    SnordTables.SST: {
        'alias': 'DS_3',
        'period': ['202422', '202423', '202424'],
        'period_type': PeriodType.year_week,
        'period_def': PeriodDef.calendar,
        'period_sap': PeriodSap.full,
        'period_tech_name': ['S_CALWK_MS'],
        'new_cols': ['DATE', 'CUSTOMER', 'EXT_ID', 'MATERIAL', 'SELLOUT', 'STOCK'],
    }
}


@dataclass(kw_only=True, slots=True)
class Period:
    ym: Optional[list[int]] = Field(
        kw_only=True,
        max_length=12,
        examples=[202403, 202404],
        default=None)
    yw: Optional[list[int]] = Field(
        kw_only=True,
        max_length=12,
        examples=[202333, 202334],
        default=None)

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


class Instance(BaseModel):
    table: SnordTables = Field(...,
                            title='Table to update',
                            examples=[SnordTables.ACTUALS],)

    alias: str = Field(title='SAP alias',
                       default=None,)

    period: Period = Field(default_factory=Period,
                            title='Period to update',
                            description='year_month or year_week',
                            examples={
                                'ym': [202303, 202304], 'yw': [202333, 202334]
                            },)

    period_type: PeriodType = Field(default=None,
                                title='Period definition',
                                description='enum of the year_month or year_week',
                                examples=[PeriodType.year_month, PeriodType.year_week],)

    period_def: PeriodDef = Field(default=None, description='Fiscal or calendar period',)

    period_sap: PeriodSap = Field(default=None, description='SAP period formatting; interval or full period and with or w/o dot-format',)

    period_tech_name: list[str] = Field(description='SAP technical name for the period', default=None,)

    new_cols: list[str] = Field(title='New columns',
                                description='Representative of the columns as they need to go into SQL',
                                default=None,)


    def model_post_init(self, __context: any) -> None:
        """ Assigns all necessary attributes needed for full update from BW all the way to SQL """

        if not all([self.period.yw, self.period.ym]):
            if SQL_META_DATA[self.table]['period_type'] == PeriodType.year_month:
                self.period_type = PeriodType.year_month
                self.period = Period(
                    ym = SQL_META_DATA[self.table]['period']
                )
            else:
                self.period_type = PeriodType.year_week
                self.period = Period(
                    yw = SQL_META_DATA[self.table]['period']
                )

        self.alias = SQL_META_DATA[self.table]['alias']

        self.period_def = SQL_META_DATA[self.table]['period_def']

        self.period_sap = SQL_META_DATA[self.table]['period_sap']

        self.period_tech_name = SQL_META_DATA[self.table]['period_tech_name']

        self.new_cols = SQL_META_DATA[self.table]['new_cols']


class Runner(BaseModel):
    instance: Instance | list[Instance] = Field(...,
                                                kw_only=True,
                                                title='Instance(s) to run',
                                                description='One or more tables to instantiate',
                                                examples=[{'table': 'actuals'}, {'table': 'sst'}],)

    period_override: Optional[Period] = Field(default=None,)


    def model_post_init(self, __context: any) -> None:
        # TODO: Doesn't handle multiple instances yet
        if self.period_override:
            self.instance.period = self.period_override


    def execute(self):
        if isinstance(self.instance, list):
            self._run_mult()
        else:
            self._run()


    # TODO: Add methods to run the instance based on types of periods and whether one or more instances are provided
    def _run(self):
        print('Running single instance')
        print(self.instance.model_dump_json(indent=2))


    def _run_mult(self):
        print('Running multiple instances')
        print(self.instance.model_dump_json(indent=2))


if __name__ == '__main__':

    m = Runner(
        # period_override=Period(ym=[202001]),
        instance={ 'table': 'actuals'},
    )


    m.execute()
    # print(m.instance[0].model_dump_json(indent=2))
    # print(m.instance[1].model_dump_json(indent=2))
