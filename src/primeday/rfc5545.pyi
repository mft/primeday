"""
type stub for rfc5545.py
"""

from datetime import (
    tzinfo,
    timezone,
)
from typing import (
    BinaryIO,
)
from icalendar import (
    Calendar,
)


utc:timezone


def createprimedaycalendarforyear(year:int, timezone:tzinfo)->Calendar:...
def output_ical(year:int, output:BinaryIO, timezone:timezone=utc)->None:...
