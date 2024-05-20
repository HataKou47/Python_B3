# 問4 奇数・偶数を判定しよう
# 整数を入力し、奇数なら「奇数」、偶数なら「偶数」と表示する

import sys
args = sys.argv

value = int(args[1])

if (value % 2 == 0):
    print("偶数", end="")
else:
    print("奇数", end="")