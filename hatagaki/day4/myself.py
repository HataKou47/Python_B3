import sys
from introduce import Intro

args = sys.argv
name = args[1]
age = int(args[2])

intro = Intro(name, age)

print(f"{intro.name_out()}")
print(f"{intro.age_out()}")