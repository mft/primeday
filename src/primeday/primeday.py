"""
Prime Day

A prime day is the day which the number YYYYMMDD is prime.
"""
import datetime
import itertools

from ._version import __version__


def isprime(yyyymmdd:int)->bool:
    """
    Return True if yyyymmdd < 25000000 is prime.
    """
    limit:int = 5000 # = sqrt(25 * pow(10, 6))
    # trial division by 2 and odd numbers
    for prime in itertools.chain((2,), range(3, limit)):
        if yyyymmdd % prime == 0:
            return False
    return True


def primedaysafter(date: datetime.date):
    """
    generate all prime days after given date (inclusive).

    The date shold be before 2500-01-01.
    """
    delta1d = datetime.timedelta(days=1)
    while date.year < 2500:
        datenum = date.year * 10000 + date.month * 100 + date.day
        if isprime(datenum):
            yield date
        date += delta1d


def primedaysforyear(year:int):
    """
    generate all prime days for given year.

    year should be less than 2500.
    """
    startdate = datetime.date(year, 1, 1)
    newyear = year + 1
    for date in primedaysafter(startdate):
        if date.year == newyear:
            break
        yield date
