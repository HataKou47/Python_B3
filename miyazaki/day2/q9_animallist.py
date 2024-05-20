# 問9 リストを操作して出力しよう
# 動物の名前リストを定義し、以下の順で操作した結果のリストを出力する
# 1,第2引数で設定したインデックスの位置に、第3引数の動物名を挿入する
# 2,リストの最後の要素を削除する
# 3,リストを昇順に並べ替える

import sys
args = sys.argv

index = int(args[1])
animal = args[2]

animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]


animals.insert(index, animal)
animals.pop()
animals.sort()

print(animals, end="")