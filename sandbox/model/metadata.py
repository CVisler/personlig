from typing import List, TypedDict
import datetime as dt
from enums import Period
from model_validators import month_, week_
from pydantic import (
    BaseModel,
    ConfigDict,
    computed_field,)
from sony import calyear_fiscyear as _conv, dotyear as _dot, sony_calendar as sc



class Pr(BaseModel):
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


    @computed_field
    @property
    def conv_last_3_months(self) -> List[month_]:
        return [int(i) for i in _conv(self.last_3_months)]


    @computed_field
    @property
    def conv_last_2_months(self) -> List[month_]:
        return [int(i) for i in _conv(self.last_2_months)]




class SQLTableContent(TypedDict):
    alias: List[str]
    period: List[month_ | week_]
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
        'period': Pr().last_3_months,
        'period_type': Period.Type.year_month,
        'period_def': Period.Def.calendar,
        'period_sap': Period.Sap.full,
        'period_tech_name': ['S_FYPOPT'],
        'new_cols': ['DATE', 'CUSTOMER', 'MATERIAL', 'QUANTITY', 'P3B_1', 'P3B', 'P5', 'MP'],
    },
    'sst': {
        'alias': [ 'DS_3' ],
        'period': Pr().last_3_weeks,
        'period_type': Period.Type.year_week,
        'period_def': Period.Def.calendar,
        'period_sap': Period.Sap.full,
        'period_tech_name': ['S_CALWK_MS'],
        'new_cols': ['DATE', 'CUSTOMER', 'EXT_ID', 'MATERIAL', 'SELLOUT', 'STOCK'],
    },
}



from json import dumps
if __name__ == '__main__':
    j = dumps(SQL_META_DATA, indent=4)
    # print(j)

    pr = Pr(
        last_3_months=[202301.0, '202010'],
    )
    print(
        pr.model_dump_json(indent=4)
    )
