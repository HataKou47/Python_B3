import sys
args = sys.argv

value = int(args[1])

if (value % 2 == 0):
    print("偶数", end="")
else:
    print("奇数", end="")