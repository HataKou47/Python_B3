# 問7 永遠の足し算
# 入力した値を繰り返して足し算し、合計がちょうど100になった場合は「Just 100!」と表示して終了し、100を超えた場合は「Over!」と表示して終了する

import sys
args = sys.argv

value = int(args[1])

sum = 0
while (sum < 100):
    sum += value
else:
    if (sum == 100):
        print("Just 100!", end="")
    else:
        print("Over!", end="")
