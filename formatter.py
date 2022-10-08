from datetime import datetime as dt
from typing import NamedTuple

class Date(NamedTuple):
    year: int
    month: int
    day: int
    hour: int
    minute: int

def tformat(datetime: dt) -> Date:
    return Date(datetime.year, datetime.month, datetime.day,\
           datetime.hour, datetime.minute)
