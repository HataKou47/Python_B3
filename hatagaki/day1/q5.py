import sys

args = sys.argv
scores = list(map(int, args[1:]))

ma = scores[0]
ja = scores[1]
en = scores[2]

if ((ma >= 70 and ja >= 70 and en >=70) or sum(scores) >= 220):
    if (ma >= 50 and ja >= 50 and en >= 50):
        print("合格", end = "")
    else:
        print("不合格", end = "")
else:
    print("不合格", end = "")

# import sys

# args = sys.argv
# scores = list(map(int, args[1:]))

# ma = scores[0]
# ja = scores[1]
# en = scores[2]

# if (((ma >= 70 and ja >= 70 and en >=70) or sum(scores) >= 220) and (ma >= 50 and ja >= 50 and en >= 50)):
#     print("合格", end = "")
# else:
#     print("不合格", end = "")