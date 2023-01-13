========
primeday
========

A prime day is the day which the number YYYYMMDD is prime.
The main repository is
https://github.com/mft/primeday

-------
install
-------

requirements
------------

icalendar >= 5

install
-------

well, there is no handy way, yet.

-------
license
-------

MIT (see License.txt)

-----
usage
-----

This package includes generators of prime days

The next example prints all prime days from today to Jan 1st 2500,
which itself is not a prime day.

```
from datetime import date
from primeday.primeday import primedaysafter

for day in primedaysafter(date.today()):
    print(day)
```

The next example prints all prime days in this year.

```
from datetime import date
from primeday.primeday import primedaysforyear

for day in primedaysforyear(date.today().year):
    print(day)
```

icalendar output modules (rfc5545.py, rfc7986.py) show example usage.
