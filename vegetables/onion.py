from vegetables.vegetable import Vegetable

class Onion(Vegetable):
    def __init__(self):
        self.seedNumber = 0

    def grow(self, number):
        self.seedNumber += number

    def getSeedNumber(self):
        return self.seedNumber