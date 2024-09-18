
from CityController import CityController
from Controller import Controller

# Ruta preferente por lo mejor
ct = CityController()
c = Controller(ct)
print(c.prims_mst()[1])
# Ruta preferente por la distacia "lineal" más corta
