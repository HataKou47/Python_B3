# 問1 自分の名前を表示しよう
# 文字列を入力すると、「Hello 入力した文字列 !」のように表示する

import sys
args = sys.argv

name = args[1]

print('Hello ' + name + ' !', end='')