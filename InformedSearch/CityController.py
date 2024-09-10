import math

from City import City


class CityController:

	def __init__(self):
		self.cities = []
		self.upload()

	# Retorna la matrix de adjacenica con los pares (id, ditance)
	def adjmatrix(self):
		return [sorted([[neigh.id, self.cdistance(city, neigh)] for neigh in city.neighs], key=lambda x: x[1]) if city.neighs else [] for city in self.cities]

	# Retorna una ciudad de acuerdo id o su nombre
	def idget(self, id):
		return self.cities[id]

	def idgetls(self, ls):
		return [self.cities[i[0]] for i in ls]

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
		names = ["Amaime", "Buga", "Cali", "Candelaria", "Corinto", "Dagua",
						"El cerrito", "Florida", "Gucari", "Ingenio Castilla",
						"Ingenio Providencia", "Jamundí", "La delfina", "Lobo Guerrero",
						"Mediacanoa", "Miranda", "Palmira", "Pradera", "Puentetierra",
						"Puerto Tejada", "Rozo", "Saladito", "San Cipriano", "San Rafael",
						"Santander de Quillinchao", "Terranova", "Vijes", "Yotoco", "Yumbo",
						"Zajon Hondo"]
		longitudes = [3.608784660653959, 3.8951920929747077, 3.4469704019148817,
									3.4126165418595154, 3.17227772436955, 3.6613985306330386,
									3.6864710402881773, 3.32309883073883, 3.7621528141000367,
									3.3746497910442455, 3.639552345807856, 3.2600029521491396, 
									3.8394089296680454, 3.76138374119755, 3.89365418542599,
									3.249999577785807, 3.5439021460011033, 3.418504427738885, 
									3.8728921587766725, 3.21921935472671, 3.6180150769312998, 
									3.4867823829738054, 3.8421294608188625, 3.0683829805293623, 
									3.012968296050415, 3.233070573732274, 3.70447047129261, 
									3.8605884950591234, 3.5475556445834346, 3.8490536483693014]
		latitudes = [-76.26852433070756, -76.30399652375277, -76.53028927603532, 
								-76.3563879404635, -76.25359597823491, -76.692446184566, 
								-76.30551953918506, -76.22507883812482, -76.33482586075226, 
								-76.26592770964912, -76.28856339975721, -76.53337220973528, 
								-76.78079005070398, -76.66007537448387, -76.36873813983884, 
								-76.22353737242904, -76.29444484752767, -76.23818130381035, 
								-76.44889441603748, -76.41467926705806, -76.38259288168372, 
								-76.6092069740518, -76.89175706534022, -76.47479647420704, 
								-76.49868921222837, -76.5256648754854, -76.43425048096273, 
								-76.37952840778865, -76.4943676881117, -76.29937212320287]

		self.cities = [(City(i, latitudes[i], longitudes[i], names[i])) for i in range(0, 30)]
		
		# Lo de los vecinos con punteros :s
		c = self.cities
		neighs = [
			[c[10], c[16]],       
			[c[14], c[29]],       
			[c[20], c[21], c[28]],
			[c[16], c[19]],       
			[c[24], c[15]],       
			[c[13], c[21]],       
			[c[8], c[10], c[20]], 
			[c[15], c[9]],        
			[c[29], c[6]],        
			[c[17], c[7]],        
			[c[6], c[0]],         
			[c[25], c[2]],        
			[c[22], c[13]],       
			[c[12], c[5], c[18]], 
			[c[18], c[1], c[27]], 
			[c[4], c[7]],         
			[c[0], c[17], c[3]],  
			[c[16], c[9]],        
			[c[13], c[14]],       
			[c[3], c[23]],        
			[c[6], c[2]],         
			[c[2], c[5]],         
			[c[12]],              
			[c[19], c[25], c[24]],
			[c[23], c[4]],        
			[c[11], c[23]],       
			[c[28], c[27]],       
			[c[26], c[14]],       
			[c[2], c[26]],        
			[c[1], c[8]]          
		]

		for i in range(0, 30):
			self.cities[i].neighs = neighs[i]
