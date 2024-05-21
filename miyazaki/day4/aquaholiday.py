import sys
import datetime as dt
# from datetime import date
from database import session
from tables import Holiday

args = sys.argv


year = int(args[1][0:4])
month = int(args[1][4:6])
day = int(args[1][6:8])
dat = dt.date(year, month, day)
adult = int(args[2])
child = int(args[3])

day_index = date.weekday()
holiday = session.query(Holiday).filter_by(holi_date=dat)

if ((day_index <= 4) or (not holiday)):
    amount_pay = (2000 * adult) + (1200 * child)
else:
    amount_pay = (2400 * adult) + (1500 * child)

print(amount_pay, end="")