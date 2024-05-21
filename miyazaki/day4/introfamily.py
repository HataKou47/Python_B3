import sys
import introduce
args = sys.argv

name = args[1]
age = args[2]
cat = args[3]

class IntroFam(introduce.Intro):
    def __init__(self, name, age, cat):
        super().__init__(name, age)
        self.cat = cat

    def cat_out(self):
        cattxt = "飼い猫の名前は、" + self.cat + "です"
        return cattxt


introduction = IntroFam(name, age, cat)

print(introduction.name_out())
print(introduction.age_out())
print(introduction.cat_out())