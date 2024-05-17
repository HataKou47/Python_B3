population = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

import sys
args = sys.argv

rank = int(args[1]) - 1

print(population[rank], end="")

#こっちもありprint(population[rank-1], end="")