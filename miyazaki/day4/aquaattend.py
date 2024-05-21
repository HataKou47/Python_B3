import sys
from datetime import date
from database import session
from tables import Attendnum
args = sys.argv

year = int(args[1][0:4])
month = int(args[1][4:6])
day = int(args[1][6:8])
dat = date(year, month, day)
adult = int(args[2])
child = int(args[3])

# 登録するデータの編集
holiday= Attendnum(
    date = dat
    seq = 
    adult = adult
    child = child
)
#INSERT処理
session.add(holiday)
#コミット
session.commit()