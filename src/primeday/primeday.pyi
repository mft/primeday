"""
type stub for primeday.py
"""

from collections.abc import Iterator
from datetime import date


def isprime(yyyymmdd: int)->bool:...
def primedaysafter(date: date)->Iterator[date]:...
def primedaysforyear(year: int)->Iterator[date]:...
