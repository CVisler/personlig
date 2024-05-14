from typing import List, TypedDict
import datetime as dt
from enums import Period
from model_validators import month_, week_
from pydantic import (
    BaseModel,
    ConfigDict,)
from sony import sony_calendar as sc


class DefaultPeriod(BaseModel):
    model_config = ConfigDict(validate_default=True) # Ensure validation of default values, thus guaranteeing output

    last_3_months: List[month_] = sc().get('last_3_months')
    last_2_months: List[month_] = sc().get('last_2_months')
    last_3_weeks: List[week_] = sc().get('last_3_weeks')
    next_4_months: List[month_] = sc().get('nx4m_incl')
    next_6_months: List[month_] = sc(
                                year=dt.datetime.now().year,
                                month=dt.datetime.now().month,
                                ranger=5).get('ranger')
    rest_fy: List[month_] = sc().get('rest_of_fy')



class SQLTableContent(TypedDict):
    alias: List[str]
    period: List[month_ | week_]
    # TODO: Study up on invariant vs covariant, i.e. using Sequence over List
    period_type: Period.Type
    period_def: Period.Def
    period_sap: Period.Sap
    period_tech_name: List[str]
    new_cols: List[str]
    technical_name: List[str]


class SQLMetaData(TypedDict):
    actuals: SQLTableContent
    sst: SQLTableContent


SQL_META_DATA: SQLMetaData = {
    'actuals': {
        'alias': [ 'DS_1' ],
        'period': DefaultPeriod().last_3_months,
        'period_type': Period.Type.year_month,
        'period_def': Period.Def.calendar,
        'period_sap': Period.Sap.interval,
        'period_tech_name': ['S_FYPOPT'],
        'new_cols': ['DATE', 'CUSTOMER', 'MATERIAL', 'QUANTITY', 'P3B_1', 'P3B', 'P5', 'MP'],
        'technical_name': ['YYEU_C_SEMFBMP_CI_SUMMARY'],
    },
    'sst': {
        'alias': [ 'DS_3' ],
        'period': DefaultPeriod().last_3_weeks,
        'period_type': Period.Type.year_week,
        'period_def': Period.Def.calendar,
        'period_sap': Period.Sap.full,
        'period_tech_name': ['S_CALWK_MS'],
        'new_cols': ['DATE', 'CUSTOMER', 'EXT_ID', 'MATERIAL', 'SELLOUT', 'STOCK'],
        'technical_name': ['SSE_CPFRSTSAM_STORHARM'],
    },
}
