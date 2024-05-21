# from introduce import Intro
from introduce import Intro

class IntroFa(Intro):
     def __init__(self, name, age, cat):
        super().__init__(name, age)
        # self.name = name
        # self.age = age
        self.cat = cat
          
    #  def name_out(self):
    #     nametxt = "私の名前は、" + self.name +"です"
    #     return nametxt

    #  def age_out(self):
    #     agetxt = "年齢は、"+ self.age +"歳です"
    #     return agetxt
     
     def cat_out(self):
        cattxt = "飼い猫の名前は、"+ self.cat +"です"
        return cattxt
     
