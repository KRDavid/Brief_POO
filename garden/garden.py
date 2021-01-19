
class Garden():
    def __init__(self):
        self.vegetables = []

    def add(self, vegetable):
        self.vegetables.append(vegetable)

    def seed(self):
        seedNumber = 0
        for vegetable in self.vegetables:
            seedNumber += vegetable.getSeedNumber()
        return seedNumber

   

