import sys

integer = int(sys.argv[1])

if integer % 2 == 0:
    print("偶数", end = "")
else:
    print("奇数", end = "")