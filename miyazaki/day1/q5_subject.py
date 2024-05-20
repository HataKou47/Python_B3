# 問5 テスト結果を判定しよう
# 数学、国語、英語の得点（整数）を入力し、次に示す2つの合格基準を同時に満たす場合は「合格」、それ以外は「不合格」と出力する
# 【合格基準】 
# 1. 3教科とも70点以上、または、合計点数が220点以上 
# 2. 1科目も50点未満がない

import sys
args = sys.argv

ma = int(args[1])
lan = int(args[2])
en = int(args[3])

passed = False

if ((ma>=70 and lan>=70 and en>=70) or (ma+lan+en >= 220)):
    if ((ma>=50)  and (lan>=50) and (en>=50)):
        passed = True

if (passed):
    print("合格", end="")
else:
    print("不合格", end="")