
class Garden():
    def __init__(self):
        self.vegetables = []

    def plant(self, vegetable):
        self.vegetables.append(vegetable)

    def seeds(self):
        seedNumber = 0
        for vegetable in self.vegetables:
            seedNumber += vegetable.getSeedNumber
