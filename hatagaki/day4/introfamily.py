import sys
from introduce import Intro

class IntroFam(Intro):
    def __init__(self, name):
        self.name = name

    def cat_out(self):
        txt = f"飼い猫の名前は、{self.name}です"
        return txt