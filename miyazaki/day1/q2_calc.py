# 問2 3つの整数を足し算しよう
# 3つの整数を入力し、その加算結果を出力する

import sys
args = sys.argv

input1 = int(args[1])
input2 = int(args[2])
input3 = int(args[3])

sum = input1 + input2 + input3

print(sum, end='')