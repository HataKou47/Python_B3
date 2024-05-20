import sys
import datetime
from datetime import date
from database import session
from tables import Holiday

args = sys.argv
the_date = args[1]
adult_num = int(args[2])
child_num = int(args[3])

fee_weekday = {'adult':2000, 'child': 1200}
fee_holiday = {'adult':2400, 'child': 1500}

dt = datetime.datetime(int(the_date[:4]), int(the_date[4:6]), int(the_date[6:]))

if dt.weekday() < 5:
    if session.query(Holiday).filter_by(holi_date=date(2024, 1, 1)).count() == 0:
        fee_dict = fee_weekday 
    else:
        fee_dict = fee_holiday
else:
    fee_dict = fee_holiday

fee = adult_num * fee_dict['adult'] + child_num * fee_dict['child']

print(fee, end = "")