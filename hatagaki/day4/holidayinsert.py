from datetime import date
from database import session
from tables import Holiday

# 登録するデータの編集
holiday= Holiday(
    holi_date = date(2022, 5, 5),
    holi_text = "お正月"
)
#INSERT処理
session.add(holiday)
#コミット
session.commit()