import sys
arg = sys.argv

input1 = int(arg[1])

if input1 % 2 == 0:
    print("偶数", end="")
else:
    print("奇数", end="")
