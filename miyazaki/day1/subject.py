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