import math

from City import City


class CityController:

	def __init__(self):
		self.cities = []

	# Retorna la matrix de adjacenica con los pares (id, ditance)
	def adjmatrix(self):
		return [[[neigh.id, self.cdistance(city, neigh)] for neigh in city.neighs].sort(key = lambda x : x[2]) for city in self.cities]

	# Retorna una ciudad de acuerdo id o su nombre -> decidan
	def idget(self, id):
		return self.cities[id]

	def cdistance(self, origin: City, destiny: City):
		return self.distance(origin.lat, origin.lat, destiny.lat, destiny.lon)

	def distance(self, lat1, lon1, lat2, lon2):
		# Convertir las coordenadas de grados a radianes
		lat1 = math.radians(lat1)
		lon1 = math.radians(lon1)
		lat2 = math.radians(lat2)
		lon2 = math.radians(lon2)

		# Diferencias de latitud y longitud
		dlat = lat2 - lat1
		dlon = lon2 - lon1

		# Fórmula de Haversine
		a = math.sin(
				dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
		c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

		# Radio de la Tierra en kilómetros (aproximadamente 6371 km)
		R = 6371.0

		# Calcular la distancia
		distance_km = R * c

		return distance_km
		
	# Calcula la distancia entre dos ciudades datos dos ids
	def idistance(self, origin, destiny):
		org = self.cities[origin]
		des = self.cities[destiny]
		return self.distance(org.lat, org.lon, des.lat, des.lon)

		

	def upload(self):
		# Agregar los nombre de manera ordenada
		names = ["Example"]
		longitudes = []
		latitudes = []
		self.cities = [(City(latitudes[i], longitudes[i], names[i])) for i in range(0, 30)]
		
		# Lo de los vecinos con punteros :s
		c = self.cities
		neighs = [[c[2], c[7]], [c[0], c[8]]]
		for i in range(0, 30):
			self.cities[i].neighs = neighs[i]
