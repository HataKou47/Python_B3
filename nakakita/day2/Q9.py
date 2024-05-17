animal = [ "giraffe", "tiger", "zebra", "elephant", "lion"]

import sys
args = sys.argv

a = int(args[1])
animal2 = args[2]

animal.insert(a, animal2)

del animal[5]
#del animal[-1] #-1で一番最後の要素になる
#animal.pop() #末尾にある要素を消すメソッド

animal.sort()

print(animal, end="")