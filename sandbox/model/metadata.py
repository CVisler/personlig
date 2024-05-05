from typing import List, TypedDict
from enums import Period, SnordTable
from validators import month_, week_


class SQLTableContent(TypedDict):
    alias: List[str]
    period: List[month_ | week_]
    period_type: Period.Type
    period_def: Period.Def
    period_sap: Period.Sap
    period_tech_name: List[str]
    new_cols: List[str]


class SQLMetaData(TypedDict):
    SnordTable.ACTUALS: SQLTableContent
    SnordTable.SST: SQLTableContent


SQL_META_DATA: SQLMetaData = {
    SnordTable.ACTUALS: {
        'alias': [ 'DS_1' ],
        'period': [202402, 202403, 202404],
        'period_type': Period.Type.year_month,
        'period_def': Period.Def.calendar,
        'period_sap': Period.Sap.full,
        'period_tech_name': ['S_FYPOPT'],
        'new_cols': ['DATE', 'CUSTOMER', 'MATERIAL', 'QUANTITY', 'P3B_1', 'P3B', 'P5', 'MP'],
    },
    SnordTable.SST: {
        'alias': [ 'DS_3' ],
        'period': [202422, 202423, 202424],
        'period_type': Period.Type.year_week,
        'period_def': Period.Def.calendar,
        'period_sap': Period.Sap.full,
        'period_tech_name': ['S_CALWK_MS'],
        'new_cols': ['DATE', 'CUSTOMER', 'EXT_ID', 'MATERIAL', 'SELLOUT', 'STOCK'],
    },
}
