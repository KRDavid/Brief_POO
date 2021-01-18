from vegetables.vegetable import Vegetable

class Tomato(Vegetable):
    def __init__(self):
        Tomato.seedNumber = 0

    def grow(self, number):
        Tomato.seedNumber += number

    def getSeedNumber(self):
        return Tomato.seedNumber