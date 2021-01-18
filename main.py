from vegetables import tomato, salad, onion
from garden import Garden

g = Garden() 
g.add(tomato.Tomato()) 
s = salad.Salad() 
s.grow(8) 
g.add(s) 
g.seed() # display 8