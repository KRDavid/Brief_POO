from garden import garden


class Gardener():
    def __init__(self):
        self.myGardens = []
        self.name = "POOlo le kebabiste"

    def buildGarden(self):
        self.myGardens.append(garden.Garden())
    
    def plant(self, garden_number:int, vegetable):
        self.myGardens[garden_number-1].add(vegetable)

    def grow(self, garden_number:int, vegetable_number:int, grow_number):
        if self.myGardens[garden_number-1].seed() < 30:
            self.myGardens[garden_number-1].vegetables[vegetable_number-1].grow(grow_number)
        else:
            print(f"Attention {self.name} il y a déjà trop de légumes dans ce jardin ! Il t'en faut un nouveau !")

    def inspection(self):
        inspection_list = []
        for garden in self.myGardens:
            

