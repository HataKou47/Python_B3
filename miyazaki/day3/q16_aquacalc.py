# 問16 水族館の入園料を計算しよう
# 料金表に従って、第2引数に日付（YYYYMMDD形式）、第3引数に大人の人数、第4引数に子供の人数を渡すと、
# 平日か土日かにより料金を算出し、合計金額を計算して出力する

import sys
import datetime as dt
args = sys.argv


year = int(args[1][0:4])
month = int(args[1][4:6])
day = int(args[1][6:8])
date = dt.date(year, month, day)
adult = int(args[2])
child = int(args[3])

day_index = date.weekday()

if (day_index <= 4):
    amount_pay = (2000 * adult) + (1200 * child)
else:
    amount_pay = (2400 * adult) + (1500 * child)

print(amount_pay, end="")