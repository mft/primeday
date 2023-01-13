"""
iCalendar output

Based on RFC 7986
"""

from datetime import (
    datetime,
)
from random import choice
from string import (
    ascii_letters,
    digits,
)
from uuid import uuid4
from icalendar import (
    Calendar,
    Event,
)
from .primeday import primedaysforyear


def createprimedaycalendarforyear(year):
    """
    Create and return a prime day calendar for given year.

    timezone is necessary to make a date to datetime.
    """
    calendar = Calendar()
    # prodid, version: required
    nonce = "".join(choice(ascii_letters + digits) for _ in range(7))
    prodid = f"primeday.py@{nonce}"
    calendar.add('prodid', prodid)
    calendar.add('version', 2.0)
    # uid and name are defined in rfc 7986
    # uuid is recommended as uid
    calendar.add('uid', str(uuid4()))
    # name can appear multiple times as language varies
    calendar.add('name', 'Prime Day', parameters={"language":"en"})
    calendar.add('name', '素数日', parameters={"language":"ja"})
    now = datetime.now()
    for i, day in enumerate(primedaysforyear(year), 1):
        event = Event()
        # dtstamp, uid, dtstart: required
        event.add('dtstamp', now)
        event.add('dtstart', day)
        # uuid is recommended as uid in rfc 7986
        event.add('uid', str(uuid4()))
        # summary, transp: optional
        event.add('summary', f'{_ordinal_en(i)} Prime Day', parameters={"language":"en"})
        event.add('transp', "TRANSPARENT")
        calendar.add_component(event)
    return calendar


def output_ical(year, output):
    """
    Output icalendar file

    The result is a icalendar file including all prime days for given year.
    Given output should be binary writable IO.

    Currently, the result file is readable by Thunderbird,
    but not readable by Apple.
    """
    calendar = createprimedaycalendarforyear(year)
    output.write(calendar.to_ical())


def _ordinal_en(num):
    """
    return English ordinal for integer num.
    """
    tens, ones = divmod(num, 10)
    if ones == 1 and tens != 1:
        return f"{num}st"
    elif ones == 2 and tens != 1:
        return f"{num}nd"
    elif ones == 3 and tens != 1:
        return f"{num}rd"
    else:
        return f"{num}th" 


if __name__ == "__main__":
    # sample code to output 2023 prime day calendar
    with open("primeday_2023.ics", "wb") as file:
        output_ical(2023, file)
