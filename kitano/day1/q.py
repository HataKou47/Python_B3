import sys
arg = sys.argv

ma = int(arg[1])
ja = int(arg[2])
en = int(arg[3])

testSum = (ma + ja + en)
#testSum >= 220 or 
if testSum >= 220 or (ma >= 70 and ja >= 70 and en >= 70):
    if (ma >= 50 and ja >= 50 and en >= 50):
        print("合格", end="")
    else:
        print("不合格", end="")
else:
    print("不合格", end="")

