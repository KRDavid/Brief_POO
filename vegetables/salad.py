from vegetables.vegetable import Vegetable

class Salad(Vegetable):
    def __init__(self):
        self.seedNumber = 0

    def grow(self, number):
        self.seedNumber += number

    def getSeedNumber(self):
        return self.seedNumber

    def __str__(self):
        return "salad"