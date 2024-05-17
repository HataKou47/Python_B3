# 問8 眠れない夜は・・・
# 「ひつじが1匹」、「ひつじが2匹」・・・「ひつじがn匹」と入力した整数の回数分繰り返す

import sys
args = sys.argv

value = int(args[1])

for i in range(value):
    print(f"ひつじが{i+1}匹\n")