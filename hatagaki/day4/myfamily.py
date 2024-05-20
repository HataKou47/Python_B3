import sys
from introfamily import IntroFam

args = sys.argv
name = args[1]
age = args[2]
cat_name = args[3]

intro = IntroFam(name, age, cat_name)

print(f"{intro.name_out()}")
print(f"{intro.age_out()}")
print(f"{intro.cat_out()}")