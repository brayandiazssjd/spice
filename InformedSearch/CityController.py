import math

from City import City


class CityController:

  def __init__(self):
    self.graph = []

  # Retorna la matrix de adjacenica con los pares (id, ditance)
  def adjmatrix(self):
    """
    for m in matrix:
      for n in m:
        n.sort(key = lambda x : x[2])
    """
    # Struture of tuple [neightbour_id, distance, latitud, longitud]
    return [[[neigh.id, self.distance(city, neigh), neigh.lat, neigh.lon] for neigh in city.neighs].sort(key = lambda x : x[2]) for city in self.cities]

  # Retorna una ciudad de acuerdo id o su nombre -> decidan
  def idget(self, name_id):
    pass

  # Calcula la distancia entre dos ciudades datos dos ids
  def distance(self, origin, destine):
    lat1, lon1 = origin
    lat2, lon2 = destine

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

  def upload(self):
    # Agregar los nombre de manera ordenada
    names = ["Example"]
    longitudes = []
    latitudes = []
    self.cities = [(City(i, latitudes[i], longitudes[i], names[i])) for i in range(0, 30)]
    
    # Lo de los vecinos con punteros :s
    c = self.cities
    neighs = [[c[2], c[7]], [c[0], c[8]]] # Se supone que cities está ordenado alfabéticamente
    for i in range(0, 30):
      self.cities[i].neighs = neighs[i]

    
  def enruteA(self, origin: City, destine: City):
    route = []

    while origin != destine:
      for neigh in origin.neighs:
        if neigh not in route: # or neigh[0] == origin
          route.append(neigh)
          origin = neigh
          break
    return route

def enruteAA(self, origin: City, destiny: City):
    route = []
    passed = []
    while origin != destiny:
      nearer = [origin, 0]
      for neigh in origin.neighs:
        distance = self.distance(neigh, destiny)
        if neigh not in passed and distance > nearer[1]:
          nearer = [neigh, distance]
          passed.append(neigh[0])
      origin = nearer[0]
      route.append(nearer)
    return route

    """
    #Recursivo
    def enrute(self, origin, destine, visited):
      if origin == destine:
          return [destine]
      next_one = self.__next(origin, destine, visited)

      return [origin] + self.enrute(next_one,destine, visited.append(origin))

    def __next(self, origin, destine, visited):
      for neigh in self.matrix[origin]:
          if neigh[0] not in visited or neigh[0] == destine:
              return neigh
      return -1
    """

