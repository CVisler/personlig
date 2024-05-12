from typing_extensions import Annotated
from pydantic import Field, AfterValidator


def test_month(v):
    __str = str(v)
    if len(__str) != 6:
        raise ValueError(f'{v} has wrong amount of digits ({len(__str)}) and not 6.')
    if int(__str[-2:]) not in range(1, 13):
        raise ValueError(f'{int(__str[-2:])} is not in the acceptable range of months')
    return v


def test_week(v):
    __str = str(v)
    if len(__str) != 6:
        raise ValueError(f'{v} has wrong amount of digits ({len(__str)}) and not 6.')
    if int(__str[-2:]) not in range(1, 54):
        raise ValueError(f'{int(__str[-2:])} is not in the acceptable range of months')
    return v


def test_dot_month(v):
    __str = str(v)
    if len(__str) != 7:
        raise ValueError(f'{v} has wrong amount of digits ({len(__str)}) and not 6.')
    if int(__str[:2]) not in range(1, 13):
        raise ValueError(f'{int(__str[-2:])} is not in the acceptable range of months')
    if int(__str[-4:]) not in range(2010, 2027):
        raise ValueError(f'{int(__str[-2:])} is not in the acceptable range of months')
    return v


def test_dot_week(v):
    __str = str(v)
    if len(__str) != 7:
        raise ValueError(f'{v} has wrong amount of digits ({len(__str)}) and not 6.')
    if int(__str[:2]) not in range(1, 54):
        raise ValueError(f'{int(__str[-2:])} is not in the acceptable range of months')
    if int(__str[-4:]) not in range(2010, 2027):
        raise ValueError(f'{int(__str[-2:])} is not in the acceptable range of months')
    return v


month_ = Annotated[int, Field(ge=201001, le=202612), AfterValidator(test_month)]
week_ = Annotated[int, Field(ge=201001, le=202612), AfterValidator(test_week)]
month_dot = Annotated[str, AfterValidator(test_dot_month)]
week_dot = Annotated[str, AfterValidator(test_dot_week)]
