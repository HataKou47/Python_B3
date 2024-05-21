from database import session
from tables import Holiday

# データを取得する
# Holidayテーブルから全てのレコードを取得します。
holidaylist=session.query(Holiday).all()

for holiday in holidaylist:
    print(holiday.holi_date,holiday.holi_text)
