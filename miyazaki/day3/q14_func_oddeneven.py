# 問14 複数の整数の奇数・偶数を判定しよう
# ３つの整数を入力し、それぞれ奇数ならば「ｘは奇数」、偶数ならば「ｘは偶数」と表示する

import sys
args = sys.argv

nums = [int(args[1]), int(args[2]), int(args[3])]

#関数を定義
def calcvalue(num):
    #あまりを算出
    mod = num % 2

    #あまりの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")

for i in nums:
    calcvalue(i)