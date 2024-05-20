import sys
from datetime import date
from database import session
from tables import Attendnum

def add_database(year, month, day, adult_num, child_num):
    dt = date(year,month,day)
    max_seq_data = session.query(Attendnum).filter_by(date = dt).order_by(Attendnum.seq.desc()).first()

    if max_seq_data.seq != None:
        seq_num = max_seq_data.seq + 1
    else:
        seq_num = 1

    data = Attendnum(
        date = dt,
        seq = seq_num,
        adult = adult_num,
        child = child_num
    )

    session.add(data)
    session.commit()

args = sys.argv
the_date = args[1]
adult_num = int(args[2])
child_num = int(args[3])

year = int(the_date[:4])
month = int(the_date[4:6])
day = int(the_date[6:])

add_database(year, month, day, adult_num, child_num)