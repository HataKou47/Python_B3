import sys
import datetime

args = sys.argv
date = args[1]
adult_num = int(args[2])
child_num = int(args[3])

fee_weekday = {'adult':2000, 'child': 1200}
fee_holiday = {'adult':2400, 'child': 1500}

dt = datetime.datetime(int(date[:4]), int(date[4:6]), int(date[6:]))

if dt.weekday() < 5:
    fee_dict = fee_weekday
else:
    fee_dict = fee_holiday

fee = adult_num * fee_dict['adult'] + child_num * fee_dict['child']

print(fee, end = "")