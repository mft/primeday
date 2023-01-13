"""
type stub for rfc7986.py
"""

from typing import (
    BinaryIO,
)
from icalendar import (
    Calendar,
)


def createprimedaycalendarforyear(year:int)->Calendar:...
def output_ical(year:int, output:BinaryIO)->None:...
def _ordinal_en(num:int)->str:...
