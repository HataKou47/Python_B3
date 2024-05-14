"""
import sys
args = sys.argv

scoreM = int(args[1])
scoreJ = int(args[2])
scoreE  = int(args[3])

sum = scoreM + scoreJ + scoreE

if (scoreM >= 70 and scoreJ >= 70 and scoreE >= 70) or (int(sum) >= 220):
    if (scoreM >= 50 and scoreJ >= 50 and scoreE >= 50):
        print("合格", end="")
else:
        print("不合格", end="")
"""

import sys
args = sys.argv

scoreM = int(args[1])
scoreJ = int(args[2])
scoreE  = int(args[3])

sum = scoreM + scoreJ + scoreE

if (scoreM >= 70 and scoreJ >= 70 and scoreE >= 70) or (int(sum) >= 220):
    if (scoreM >= 50 and scoreJ >= 50 and scoreE >= 50):
        print("合格", end="")
    else:
        print("不合格", end="")
else:
    print("不合格", end="")
