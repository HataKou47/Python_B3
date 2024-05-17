import sys
args = sys.argv

index = int(args[1])
animal = args[2]

animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]


animals.insert(index, animal)
animals.pop()
animals.sort()

print(animals, end="")