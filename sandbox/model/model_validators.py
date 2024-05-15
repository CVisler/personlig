from typing_extensions import Annotated
from pydantic import AfterValidator


def test_month(v):
    if isinstance(v, list):
        for i in v:
            __str = str(i)
            if len(__str) != 6:
                raise ValueError(f'{v} has wrong amount of digits ({len(__str)}) and not 6.')
            if int(__str[:4]) not in range(2010, 2027):
                raise ValueError(f'{int(__str[:4])} is not in the acceptable range of years')
            if int(__str[-2:]) not in range(1, 13):
                raise ValueError(f'{int(__str[-2:])} is not in the acceptable range of months')
    else:
        __str = str(v)
        if len(__str) != 6:
            raise ValueError(f'{v} has wrong amount of digits ({len(__str)}) and not 6.')
        if int(__str[:4]) not in range(2010, 2027):
            raise ValueError(f'{int(__str[:4])} is not in the acceptable range of years')
        if int(__str[-2:]) not in range(1, 13):
            raise ValueError(f'{int(__str[-2:])} is not in the acceptable range of months')
    return v


def test_week(v):
    if isinstance(v, list):
        for i in v:
            __str = str(i)
            if len(__str) != 6:
                raise ValueError(f'{v} has wrong amount of digits ({len(__str)}) and not 6.')
            if int(__str[:4]) not in range(2010, 2027):
                raise ValueError(f'{int(__str[:4])} is not in the acceptable range of years')
            if int(__str[-2:]) not in range(1, 54):
                raise ValueError(f'{int(__str[-2:])} is not in the acceptable range of months')
    else:
        __str = str(v)
        if len(__str) != 6:
            raise ValueError(f'{v} has wrong amount of digits ({len(__str)}) and not 6.')
        if int(__str[:4]) not in range(2010, 2027):
            raise ValueError(f'{int(__str[:4])} is not in the acceptable range of years')
        if int(__str[-2:]) not in range(1, 54):
            raise ValueError(f'{int(__str[-2:])} is not in the acceptable range of months')
    return v


def test_dot_month(v):
    if isinstance(v, list):
        for i in v:
            __str = str(i)
            if len(__str) != 7:
                raise ValueError(f'{v} has wrong amount of digits ({len(__str)}) and not 6.')
            if int(__str[:2]) not in range(1, 13):
                raise ValueError(f'{int(__str[:2])} is not in the acceptable range of months')
            if int(__str[-4:]) not in range(2010, 2027):
                raise ValueError(f'{int(__str[-4:])} is not in the acceptable range of years')
    else:
        __str = str(v)
        if len(__str) != 7:
            raise ValueError(f'{v} has wrong amount of digits ({len(__str)}) and not 6.')
        if int(__str[:2]) not in range(1, 13):
            raise ValueError(f'{int(__str[:2])} is not in the acceptable range of months')
        if int(__str[-4:]) not in range(2010, 2027):
            raise ValueError(f'{int(__str[-4:])} is not in the acceptable range of years')
    return v


def test_dot_week(v):
    if isinstance(v, list):
        for i in v:
            __str = str(i)
            if len(__str) != 7:
                raise ValueError(f'{v} has wrong amount of digits ({len(__str)}) and not 6.')
            if int(__str[:2]) not in range(1, 54):
                raise ValueError(f'{int(__str[:2])} is not in the acceptable range of months')
            if int(__str[-4:]) not in range(2010, 2027):
                raise ValueError(f'{int(__str[-4:])} is not in the acceptable range of years')
    else:
        __str = str(v)
        if len(__str) != 7:
            raise ValueError(f'{v} has wrong amount of digits ({len(__str)}) and not 6.')
        if int(__str[:2]) not in range(1, 54):
            raise ValueError(f'{int(__str[:2])} is not in the acceptable range of months')
        if int(__str[-4:]) not in range(2010, 2027):
            raise ValueError(f'{int(__str[-2:])} is not in the acceptable range of years')
    return v


month_ = Annotated[int, AfterValidator(test_month)]
week_ = Annotated[int, AfterValidator(test_week)]
month_dot = Annotated[str, AfterValidator(test_dot_month)]
week_dot = Annotated[str, AfterValidator(test_dot_week)]
