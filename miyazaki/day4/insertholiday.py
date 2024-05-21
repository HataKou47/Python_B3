from datetime import date
from database import session
from tables import Holiday


# 登録するデータの編集
holidays = [Holiday(holi_date = date(2023, 1, 1), holi_text = "正月"),
            Holiday(holi_date = date(2023, 1, 8), holi_text = "お正月"),
            Holiday(holi_date = date(2023, 2, 11), holi_text = "お正月"),
            Holiday(holi_date = date(2023, 2, 23), holi_text = "お正月"),
            Holiday(holi_date = date(2023, 3, 20), holi_text = "お正月"),
            Holiday(holi_date = date(2023, 4, 29), holi_text = "お正月"),
            Holiday(holi_date = date(2023, 5, 3), holi_text = "お正月"),
            Holiday(holi_date = date(2023, 5, 4), holi_text = "お正月"),
            Holiday(holi_date = date(2023, 5, 5), holi_text = "お正月"),
            Holiday(holi_date = date(2023, 7, 15), holi_text = "お正月"),
            Holiday(holi_date = date(2023, 8, 11), holi_text = "お正月"),
            Holiday(holi_date = date(2023, 9, 16), holi_text = "お正月"),
            Holiday(holi_date = date(2023, 9, 22), holi_text = "お正月"),
            Holiday(holi_date = date(2023, 10, 14), holi_text = "お正月"),
            Holiday(holi_date = date(2023, 11, 3), holi_text = "お正月"),
            Holiday(holi_date = date(2023, 11, 23), holi_text = "お正月"),
            ]

#INSERT処理
for holiday in holidays:
    session.add(holiday)

#コミット
session.commit()
