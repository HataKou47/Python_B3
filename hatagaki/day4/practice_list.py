from database import session
from tables import Attendnum

# データを取得する
attendlist=session.query(Attendnum).all()

for data in attendlist:
    print(data.date,data.seq,data.adult,data.child)