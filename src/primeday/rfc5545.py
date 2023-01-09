"""
iCalendar output

Based on RFC 5545
"""

import datetime
import random
import string
import typing
import icalendar
from .primeday import primedaysforyear


utc = datetime.timezone(datetime.timedelta(minutes=0))


def createprimedaycalendarforyear(year:int, timezone:datetime.tzinfo)->icalendar.Calendar:
    """
    Create and return a prime day calendar for given year.

    timezone is necessary to make a date to datetime.
    """
    calendar:icalendar.Calendar = icalendar.Calendar()
    # prodid, version: required
    nonce = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(7))
    prodid = f"primeday.py@{nonce}"
    calendar.add('prodid', prodid)
    calendar.add('version', 2.0)
    calendar.add('calscale', 'GREGORIAN')
    delta1d = datetime.timedelta(days=1)
    now = datetime.datetime.now(timezone)
    for day in primedaysforyear(year):
        event = icalendar.Event()
        event.add('summary', 'Prime Day')
        # dtstamp, uid, dtstart: required
        event.add('dtstamp', now)
        dt = datetime.datetime(year, day.month, day.day, 0, 0, 0, tzinfo=timezone)
        event.add('dtstart', dt)
        uid = f"{dt.strftime('%Y%m%d')}-{prodid}"
        event.add('uid', uid)
        # duration, transp: optional
        event.add('duration', delta1d)
        event.add('transp', "TRANSPARENT")
        calendar.add_component(event)
    return calendar


def output_ical(year:int, output:typing.BinaryIO, timezone=utc):
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
        jst = datetime.timezone(datetime.timedelta(hours=9))
        output_ical(2023, file, timezone=jst)
