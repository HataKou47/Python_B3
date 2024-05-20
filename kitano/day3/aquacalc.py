import sys
import datetime

# today = datetime.date.today()

# print(f'日付: {today}, 曜日{today.weekday()}')

args = sys.argv

day = args[1]
adult_number = int(args[2])
child_number = int(args[3])

year = day[0:4]
month = day[4:6]
day = day[6:9]

dt = datetime.datetime(int(year), int(month), int(day))

if dt.weekday() <= 4:
    price = adult_number * 2000 + child_number * 1200
else:
    price = adult_number * 2400 + child_number * 1500

print(price)

