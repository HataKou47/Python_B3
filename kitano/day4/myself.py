import sys
from introduce import Intro

args = sys.argv

intro = Intro(args[1], args[2])

print(intro.name_out())
print(intro.age_out())