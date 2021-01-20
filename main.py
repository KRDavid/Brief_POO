from vegetables import tomato, salad, onion
from garden import garden, gardener


gardenguy = gardener.Gardener()

gardenguy.buildGarden()

gardenguy.plant(1, tomato.Tomato())
gardenguy.grow(1, 1, 5)
gardenguy.plant(1, salad.Salad())
gardenguy.grow(1, 2, 25)
gardenguy.grow(1, 1, 5)

gardenguy.buildGarden()

gardenguy.plant(2, tomato.Tomato())
gardenguy.grow(2, 1, 10)
gardenguy.plant(2, salad.Salad())
gardenguy.grow(2, 2, 5)

gardenguy.inspection()

# g = garden.Garden() 
# g.add(tomato.Tomato()) 
# s = salad.Salad() 
# s.grow(8) 
# g.add(s) 
# print(g.seed()) # display 8
