# 問12 英文のn番目の単語は？
# 英文と取り出したい単語の位置を入力し、指定した位置の単語を出力する

import sys
args = sys.argv

english = args[1]
index = int(args[2])

english = english.split()

print(english[index-1], end="")
