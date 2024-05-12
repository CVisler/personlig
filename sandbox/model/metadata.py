from typing import List, Sequence, TypedDict
import datetime as dt
from enums import Period
from model_validators import month_, week_, month_dot, week_dot
from pydantic import (
    BaseModel,
    field_validator,
    Field,
    ConfigDict,)
from sony import sony_calendar as sc


class BasePeriod(BaseModel):
    model_config = ConfigDict(validate_default=True) # Ensure validation of default values, thus guaranteeing output

    month: List[month_] = Field(
        kw_only=True,
        max_length=12, # Max list length
        examples=[202403, 202404],
        default_factory=list,)


    week: List[week_] = Field(
        kw_only=True,
        max_length=3, # Max list length
        examples=[202333, 202334],
        default_factory=list,)

    last_3_months: List[month_] = sc().get('last_3_months')
    last_2_months: List[month_] = sc().get('last_2_months')
    last_3_weeks: List[week_] = sc().get('last_3_weeks')
    next_4_months: List[month_] = sc().get('nx4m_incl')
    next_6_months: List[month_] = sc(
                                year=dt.datetime.now().year,
                                month=dt.datetime.now().month,
                                ranger=5).get('ranger')
    rest_fy: List[month_] = sc().get('rest_of_fy')


    @field_validator('month', 'week', mode='before')
    @classmethod
    def check_list(cls, v):
        if not isinstance(v, list):
            return [v]
        else:
            return v


class SQLTableContent(TypedDict):
    alias: List[str]
    period: List[month_ | week_]
    # TODO: Study up on invariant vs covariant, i.e. using Sequence over List
    period_sap_entry: Sequence[month_ | week_ | month_dot | week_dot]
    period_type: Period.Type
    period_def: Period.Def
    period_sap: Period.Sap
    period_tech_name: List[str]
    new_cols: List[str]


class SQLMetaData(TypedDict):
    actuals: SQLTableContent
    sst: SQLTableContent


SQL_META_DATA: SQLMetaData = {
    'actuals': {
        'alias': [ 'DS_1' ],
        'period': BasePeriod().last_3_months,
        'period_sap_entry': [202406, 202407, 202408], # TODO: Make this dynamic by for example using same model-setup as in m.py
        'period_type': Period.Type.year_month,
        'period_def': Period.Def.calendar,
        'period_sap': Period.Sap.dot_interval,
        'period_tech_name': ['S_FYPOPT'],
        'new_cols': ['DATE', 'CUSTOMER', 'MATERIAL', 'QUANTITY', 'P3B_1', 'P3B', 'P5', 'MP'],
    },
    'sst': {
        'alias': [ 'DS_3' ],
        'period': BasePeriod().last_3_weeks,
        'period_sap_entry': BasePeriod().last_3_weeks,
        'period_type': Period.Type.year_week,
        'period_def': Period.Def.calendar,
        'period_sap': Period.Sap.full,
        'period_tech_name': ['S_CALWK_MS'],
        'new_cols': ['DATE', 'CUSTOMER', 'EXT_ID', 'MATERIAL', 'SELLOUT', 'STOCK'],
    },
}
