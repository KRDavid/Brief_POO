from vegetables.vegetable import Vegetable

class Salad(Vegetable):
    def __init__(self):
        Salad.seedNumber = 0

    def grow(self, number):
        Salad.seedNumber += number

    def getSeedNumber(self):
        return Salad.seedNumber