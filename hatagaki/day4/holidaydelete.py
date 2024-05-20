from datetime import date
from database import session
from tables import Holiday

# 削除するデータを取得する
result = session.query(Holiday).filter_by(holi_date=date(2022, 5, 5)).delete()

#コミット
session.commit()