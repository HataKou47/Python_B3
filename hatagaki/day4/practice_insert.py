from datetime import date
from database import session
from tables import Holiday

months = [1,1,2,2,3,4,5,5,5,7,8,9,9,10,11,11]
days = [1,8,11,23,20,29,3,4,5,15,11,16,22,14,3,23]
names = ["元旦","成人の日","建国記念の日","天皇誕生日","春分の日","昭和の日",
         "憲法記念日","みどりの日","こどもの日","海の日","山の日","敬老の日",
         "秋分の日","スポーツの日","文化の日","勤労感謝の日"]

for month, day, name in zip(months, days, names):
    holiday = Holiday(
        holi_date = date(2024, month, day),
        holi_text = name
    )

    session.add(holiday)

#コミット
session.commit()