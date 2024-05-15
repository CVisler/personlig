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



# TODO: Study up on invariant vs covariant, i.e. using Sequence over List
class SQLTableContent(TypedDict):
    alias: str
    period: List[month_ | week_]
    period_type: Period.Type
    period_def: Period.Def
    period_sap: Period.Sap
    period_tech_name: List[str]
    new_cols: List[str]
    technical_name: List[str]


class SQLMetaData(TypedDict):
    actuals: SQLTableContent
    koro_sellout: SQLTableContent
    marketing_fc: SQLTableContent
    market_size: SQLTableContent
    ranging: SQLTableContent
    sst: SQLTableContent
    sst_month: SQLTableContent
    orders: SQLTableContent


SQL_META_DATA: SQLMetaData = {
    'actuals': {
        'alias': 'DS_1',
        'period': DefaultPeriod().last_3_months,
        'period_type': Period.Type.year_month,
        'period_def': Period.Def.calendar,
        'period_sap': Period.Sap.interval,
        'period_tech_name': ['S_FYPOPT'],
        'new_cols': ['DATE', 'CUSTOMER', 'MATERIAL', 'QUANTITY', 'P3B_1', 'P3B', 'P5', 'MP'],
        'technical_name': ['YYEU_C_SEMFBMP_CI_SUMMARY'],
    },
    'koro_sellout': {
        'alias': 'DS_10',
        'period': DefaultPeriod().next_6_months,
        'period_type': Period.Type.year_month,
        'period_def': Period.Def.calendar,
        'period_sap': Period.Sap.dot_full,
        'period_tech_name': ['S_MTHSO'],
        'new_cols': ['DATE', 'MATERIAL', 'SELLOUT'],
        'technical_name': ['ZZQU_ZMSC11_VALIDATION'],
    },
    'marketing_fc': {
        'alias': 'DS_11',
        'period': DefaultPeriod().next_6_months,
        'period_type': Period.Type.year_month,
        'period_def': Period.Def.calendar,
        'period_sap': Period.Sap.dot_interval,
        'period_tech_name': ['S_MONMI'],
        'new_cols': ['DATE', 'MATERIAL', 'QUANTITY', 'P5', 'MP', 'P3', 'P3B'],
        'technical_name': ['SNORUP_SEMFQTYM_CALMONTH_EUR'],
    },
    'market_size': {
        'alias': 'DS_2',
        'period': DefaultPeriod().next_6_months,
        'period_type': Period.Type.year_month,
        'period_def': Period.Def.calendar,
        'period_sap': Period.Sap.dot_full,
        'period_tech_name': ['ZZVA_0CALMONTH_MSEL'],
        'new_cols': ['DATE', 'SEGMENT', 'SIZE'],
        'technical_name': ['ZZQU_ZMSC1MS35_CHECK'],
    },
    'ranging': {
        'alias': 'DS_8',
        'period': DefaultPeriod().rest_fy,
        'period_type': Period.Type.year_month,
        'period_def': Period.Def.fiscal,
        'period_sap': Period.Sap.dot_interval,
        'period_tech_name': [''],
        'new_cols': ['DATE', 'SAG_CODE', 'MATERIAL', 'RANGING'],
        'technical_name': ['YYXX_B_ZMSD12'],
    },
    'sst': {
        'alias': 'DS_3',
        'period': DefaultPeriod().last_3_weeks,
        'period_type': Period.Type.year_week,
        'period_def': Period.Def.calendar,
        'period_sap': Period.Sap.interval,
        'period_tech_name': ['S_CALWK_MS'],
        'new_cols': ['DATE', 'CUSTOMER', 'EXT_ID', 'MATERIAL', 'SELLOUT', 'STOCK'],
        'technical_name': ['SSE_CPFRSTSAM_STORHARM'],
    },
    'sst_month': {
        'alias': 'DS_12',
        'period': DefaultPeriod().last_3_weeks,
        'period_type': Period.Type.year_week,
        'period_def': Period.Def.calendar,
        'period_sap': Period.Sap.dot_interval,
        'period_tech_name': ['0I_CWEEK'],
        'new_cols': ['DATE', 'CUSTOMER', 'EXT_ID', 'MATERIAL', 'SELLOUT'],
        'technical_name': ['SNORUP_MULTI005_SST_CORE'],
    },
    'orders': {
        'alias': 'DS_4;DS_5;DS_6;DS_7',
        'period': DefaultPeriod().next_4_months,
        'period_type': Period.Type.year_month,
        'period_def': Period.Def.fiscal,
        'period_sap': Period.Sap.dot_full,
        'period_tech_name': ['S_PER_A', 'S_FYPOPT'],
        'new_cols': ["DATE", "CUSTOMER", "MATERIAL", "DMDQTY", "DMDNS", "DMDVAL", "POTQTY", "POTNS", "POTVAL"],
        'technical_name': ['YYEU_C_EUSODM_ORDERPOS_EU'],
    },
}
