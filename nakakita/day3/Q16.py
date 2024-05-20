heijitu = {'大人':2000,'子供':1200}
weekend ={'大人':2400,'子供':1500}

import sys
args = sys.argv

date = args[1]
otona = int(args[2])
kodomo = int(args[3])

import datetime

year = int(date[:4])
month = int(date[4:6])
day = int(date[6:8])

dt = datetime.datetime(int(date[:4]), int(date[4:6]), int(date[6:8]))


if  dt.weekday() <= 4:
    sum_price = (otona * heijitu['大人']) + (kodomo * heijitu['子供'])
else:
    sum_price = (otona * weekend['大人']) + (kodomo * weekend['子供'])

print(sum_price)