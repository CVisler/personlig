from enum import StrEnum

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


class SnordTable(StrEnum):
    actuals = 'actuals'
    sst = 'sst'
