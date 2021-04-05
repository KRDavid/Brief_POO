import unittest
from garden import garden, gardener
from vegetables import tomato

class Testing_gardener(unittest.TestCase):
    
    jardinier = gardener.Gardener()

    def test_0_gardener_content(self):
        self.assertEqual(self.jardinier.myGardens, [])
        self.assertEqual(self.jardinier.name, "POOlo le kebabiste")

    def test_1_add_garden(self):
        self.jardinier.buildGarden()
        self.assertTrue(type(self.jardinier.myGardens[0] == garden.Garden))

    def test_2_plant(self):
        self.jardinier.plant(1, tomato.Tomato())
        self.assertTrue(type(self.jardinier.myGardens[0].vegetables[0] == tomato.Tomato))
    
    def test_3_grow(self):
        self.jardinier.grow(1,1,10)
        self.assertEqual(self.jardinier.myGardens[0].vegetables[0].seedNumber, 10)


class Testing_garden(unittest.TestCase):
    
    jardin = garden.Garden()

    def test_0_garden_content(self):
        self.assertEqual(self.jardin.vegetables, [])

    def test_1_garden_content(self):
        self.jardin.add(tomato.Tomato())
        self.jardin.vegetables[0].grow(10)
        self.assertEqual(self.jardin.vegetables[0].seedNumber, 10)

    def test_2_inspection(self):
        self.assertTrue(type(self.jardin.seed()) == int)
        self.assertEqual(self.jardin.seed(), 10)


class Testing_tomato(unittest.TestCase):
    tomate = tomato.Tomato()

    def test_0_seednumber(self):
        self.assertEqual(self.tomate.seedNumber, 0)

    def test_1_grow(self):
        self.tomate.grow(10)
        self.assertEqual(self.tomate.seedNumber, 10)
    
    def test_2_getseednumber(self):
        self.assertTrue(type(self.tomate.getSeedNumber()) == int)
        self.assertEqual(self.tomate.getSeedNumber(), 10)


if __name__ == '__main__':
    unittest.main()