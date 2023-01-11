"""
iCalendar output

Based on RFC 5545
"""

from datetime import (
    datetime,
    timedelta,
    timezone,
)
from random import choice
from string import (
    ascii_letters,
    digits,
)
from icalendar import (
    Calendar,
    Event,
)
from .primeday import primedaysforyear


utc = timezone(timedelta(minutes=0))


def createprimedaycalendarforyear(year, timezone):
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
    calendar.add('calscale', 'GREGORIAN')
    delta1d = timedelta(days=1)
    now = datetime.now(timezone)
    for day in primedaysforyear(year):
        event = Event()
        event.add('summary', 'Prime Day')
        # dtstamp, uid, dtstart: required
        event.add('dtstamp', now)
        dt = datetime(year, day.month, day.day, 0, 0, 0, tzinfo=timezone)
        event.add('dtstart', dt)
        uid = f"{dt.strftime('%Y%m%d')}-{prodid}"
        event.add('uid', uid)
        # duration, transp: optional
        event.add('duration', delta1d)
        event.add('transp', "TRANSPARENT")
        calendar.add_component(event)
    return calendar


def output_ical(year, output, timezone=utc):
    """
    Output icalendar file

    The result is a icalendar file including all prime days for given year.
    Given output should be binary writable IO.

    Currently, the result file is readable by Thunderbird,
    but not readable by Apple.
    """
    calendar = createprimedaycalendarforyear(year, timezone)
    output.write(calendar.to_ical())


if __name__ == "__main__":
    # sample code to output JST (Japan Standart Time) calendar
    with open("primeday_jst.ics", "wb") as file:
        jst = timezone(timedelta(hours=9))
        output_ical(2023, file, timezone=jst)
