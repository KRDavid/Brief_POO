from vegetables.vegetable import Vegetable

class Onion(Vegetable):
    def __init__(self):
        Onion.seedNumber = 0

    def grow(self, number):
        Onion.seedNumber += number

    def getSeedNumber(self):
        return Onion.seedNumber