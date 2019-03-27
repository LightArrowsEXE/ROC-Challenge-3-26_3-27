import calendar
import datetime
import time
import argparse
import texttable as tt
import re

from birthdate import birthdate
# birthdate = | name | year | month | day |

parser = argparse.ArgumentParser()
parser.add_argument("-Y", "--year", help="set specific year", type=int)
parser.add_argument("-M", "--month", help="set specific month", type=int)
args = parser.parse_args()


def allMonths():
    for m in calendar.month_name:
        return(m)


def countDays(year, month):
    return calendar.monthrange(year, month)


def currentMonth(year, month):
    for d in birthdate:
        if d[3] == month:
            return d


def calculateAge(birthyear, birthmonth, birthday):
    return year - birthyear - ((month, day) < (birthmonth, birthday))


year, month, day = time.strftime("%Y,%m,%d").split(',')
year = int(year)
month = int(month)
day = int(day)

if args.year:
    year = args.year
if args.month:
    month = args.month

test = currentMonth(year, month)

tab = tt.Texttable()
tab.set_cols_width(40)
tab.header(allMonths())

for d in birthdate:
    if d[2]:
        age = calculateAge(d[1], d[2], d[3])
        print(age)
        tab.add_row(
            f"{d[2]} - {d[0]}'s birthday! {d[0]} is turning {age} this year!")

draw = tab.draw()
print(draw)
