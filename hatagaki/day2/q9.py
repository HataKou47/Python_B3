import sys

args = sys.argv

idx = int(args[1])
animal_name = args[2]

animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]

# 1
animals.insert(idx, animal_name)

# 2
animals = animals[:len(animals) - 1]

# 3
animals.sort()

print(animals, end = "")