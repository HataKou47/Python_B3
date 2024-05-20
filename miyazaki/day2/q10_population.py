# 問10 人口ランキングｎ位はどこ？
# タプルに世界人口ランキングを定義し、引数に指定した順位の国名を出力する

import sys
args = sys.argv

index = int(args[1])

Population_ranking = ["China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico"]


print(Population_ranking[index-1], end="")