from enum import StrEnum

class Period:
    class Type(StrEnum):
        year_month = 'year_month'
        year_week = 'year_week'
    class Def(StrEnum):
        fiscal = 'fiscal'
        calendar = 'calendar'
    class Sap(StrEnum):
        interval = 'interval' # means only the first and last period indices must be present
        full = 'full' # means all period indices must be present
        dot_interval = 'dot_interval' # means only the first and last period indices must be present with the dot syntax
        dot_full = 'dot_full' # means all period indices must be present with the dot syntax


class SnordTable(StrEnum):
    actuals = 'actuals'
    sst = 'sst'
