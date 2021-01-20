from vegetables.vegetable import Vegetable

class Tomato(Vegetable):
    def __init__(self):
        self.seedNumber = 0

    def grow(self, number):
        self.seedNumber += number

    def getSeedNumber(self):
        return self.seedNumber

    def __str__(self):
        return "tomato"