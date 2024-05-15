import sys
i =  int(sys.argv[1])
animalname = sys.argv[2]

animal =["giraffe", "tiger", "zebra", "elephant", "lion"]

#1
animal.insert(i, animalname)

#2
animal.pop()


#3
animal.sort()
print(animal, end = "")