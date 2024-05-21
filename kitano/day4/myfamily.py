import sys
from IntroFam import IntroFa

args = sys.argv

intro = IntroFa(args[1], args[2], args[3])

print(intro.name_out())
print(intro.age_out())
print(intro.cat_out())
