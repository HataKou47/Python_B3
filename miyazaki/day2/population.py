import sys
args = sys.argv

index = int(args[1])

Population_ranking = ["China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico"]


print(Population_ranking[index-1], end="")