from vegetables import tomato, salad, onion
from garden import garden
from garden import gardener

gardenguy = gardener.Gardener()

gardenguy.buildGarden()

gardenguy.plant(1, tomato.Tomato())
gardenguy.plant(1, salad.Salad())



# g = garden.Garden() 
# g.add(tomato.Tomato()) 
# s = salad.Salad() 
# s.grow(8) 
# g.add(s) 
# print(g.seed()) # display 8

# t = tomato.Tomato()
# t.grow(10)

# print(g.seed())