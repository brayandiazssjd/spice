
from CityController import CityController
from Controller import Controller

# Ruta preferente por lo mejor
ct = CityController()
c = Controller(ct)
for edges in c.prims_mst()[0]:
	for edge in edges:
		print(edge.to)
	print("--")

# Ruta preferente por la distacia "lineal" más corta
