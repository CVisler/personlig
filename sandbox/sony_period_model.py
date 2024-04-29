from pydantic import field_validator, BaseModel, Field
from pydantic.dataclasses import dataclass
from enum import StrEnum
from typing import Optional, List, TypedDict


class SnordTables(StrEnum):
    ACTUALS = 'actuals'
    SST = 'sst'


class PeriodDef(StrEnum):
    year_month = 'year_month'
    year_week = 'year_week'


class SQLTableContent(TypedDict):
    alias: str
    period: list[str] # Why is this a list of strings? Because the sony_calendar() is set up to return strings I believe
    period_def: PeriodDef
    period_tech_name: list[str]
    new_cols: list[str]


class SQLMetaData(TypedDict):
    SnordTables.ACTUALS: SQLTableContent
    SnordTables.SST: SQLTableContent


SQL_META_DATA: SQLMetaData = {
    SnordTables.ACTUALS: {
        'alias': 'DS_1',
        'period': ['202402', '202403', '202404'],
        'period_def': PeriodDef.year_month,
        'period_tech_name': ['S_FYPOPT'],
        'new_cols': ['DATE', 'CUSTOMER', 'MATERIAL', 'QUANTITY', 'P3B_1', 'P3B', 'P5', 'MP'],
    },
    SnordTables.SST: {
        'alias': 'DS_3',
        'period': ['202422', '202423', '202424'],
        'period_def': PeriodDef.year_week,
        'period_tech_name': ['S_CALWK_MS'],
        'new_cols': ['DATE', 'CUSTOMER', 'EXT_ID', 'MATERIAL', 'SELLOUT', 'STOCK'],
    }
}


@dataclass(kw_only=True, slots=True)
class PeriodType:
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


class Process(BaseModel):
    """ One process should be instantiated for each SAP alias to update.
    ---
    WoW: create an instance representation of the SQL table you wish to update by providing table name and period.
    """
    table: SnordTables = Field(...,
                            title='Table to update',
                            examples=[SnordTables.ACTUALS],)
    alias: str = Field(title='SAP alias',
                       default=None,)
    period: PeriodType = Field(default_factory=PeriodType,
                            title='Period to update',
                            description='year_month or year_week',
                            examples={
                                'ym': [202303, 202304], 'yw': [202333, 202334]
                            },)
    period_def: PeriodDef = Field(default=None,
                                title='Period definition',
                                description='year_month or year_week',
                                examples=[PeriodDef.year_month, PeriodDef.year_week],)
    period_tech_name: list[str] = Field(description='SAP technical name for the period',
                                        default=None,)
    new_cols: list[str] = Field(title='New columns',
                                description='Representative of the columns as they need to go into SQL',
                                default=None,)


    def model_post_init(self, __context: any) -> None:
        """ Assigns all necessary attributes needed for full update from BW all the way to SQL """

        if not all([self.period.yw, self.period.ym]):
            if SQL_META_DATA[self.table]['period_def'] == PeriodDef.year_month:
                self.period_def = PeriodDef.year_month
                self.period = PeriodType(
                    ym = SQL_META_DATA[self.table]['period']
                )
            else:
                self.period_def = PeriodDef.year_week
                self.period = PeriodType(
                    yw = SQL_META_DATA[self.table]['period']
                )

        self.alias = SQL_META_DATA[self.table]['alias']

        self.period_tech_name = SQL_META_DATA[self.table]['period_tech_name']

        self.new_cols = SQL_META_DATA[self.table]['new_cols']


    # TODO: Consider if particular methods of the class should be called depending on the table and thus the settings required to manipulate the period
    # i.e. if we need first and last slice of a dot-fiscal year or something like that
    #
    # TODO: What meta data is needed to be able to update the table? 
    # [ fiscal-year ]
    # [ dot-year ]
    # [ orders ]

    def update(self):
        """ Begin the update process """
        print(f'\nUpdating... {self.table}', end='\n\n')


    def display(self):
        print(
            self.model_dump_json(indent=4)
        )


if __name__ == '__main__':
    process_actuals = Process(
        table='actuals',
        # period=PeriodType(
        #     ym=SQL_META_DATA[SnordTables.ACTUALS]['period']
        # ),
    )

    process_actuals.update()
    process_actuals.display()
