# 問3 嫌いな食べ物を表示しよう
# 嫌いな食べ物を入力すると、「I don’t like 入力した文字列」を出力する

import sys
args = sys.argv

food = args[1]

print("I don't like \"" + food + "\"", end="")