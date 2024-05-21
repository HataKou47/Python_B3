class Intro:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def name_out(self):
        txt = f"私の名前は、{self.name}です"
        return txt

    def age_out(self):
        txt = f"年齢は、{self.age}です"
        return txt