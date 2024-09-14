from CityController import CityController
import heapq

class Controller:

	def __init__(self, matrix, ct: CityController):
		self.__matrix = matrix
		self.__ct = ct

	# Returna el par solución [[ids], [distances]] para A
	# TODO: optimize using a binary passed list
	# TODO: change return to [[cities: City], distance:int]
	def enruteA(self, origin, destine): 
		diss = []
		passed = []
		ids = []		
		while origin != destine:
			for neigh in self.__matrix[origin]:
				if neigh[0] not in passed:  # or neigh[0] == origin
					ids.append(neigh[0])
					passed.insert(0, neigh[0])
					diss.append(neigh[1])
					origin = neigh[0]
					break
		return [ids, diss]

	# Returna el par solución [[ids], [distances]] para A*
	# TODO: optimize using a binary
	# TODO: change return to [[cities: City], distance:int]
	# TODO: change index for sub list "[:]"
	def enruteAA(self, origin: int, destiny: int):
		ids = [origin]
		passed = [origin]
		diss = []
		
		while origin != destiny:
			neigh = self.__matrix[origin][0]
			# nearer = [neighbour, distance from origin to neighbour]
			nearer = [neigh,	self.__ct.idistance(neigh[0], destiny)]
			for i in range(1, len(self.__matrix[origin])):
				neigh = self.__matrix[origin][i]
				distance = self.__ct.idistance(neigh[0], destiny)

				if neigh[0] not in passed:
					passed.insert(0, neigh[0])
					if (distance + neigh[1]) < nearer[0][1] + nearer[1]:
						nearer = [neigh, distance]
			origin = nearer[0][0]
			ids.append(nearer[0][0])
			diss.append(nearer[0][1])
		return [ids, diss] 

	def lazy_prim(self):
		mst = []
		count, cost = 0, 0
		n = len(self.__matrix)
		visited = [False for i in range(n)]
		pq = []

		while not pq and count < n:
			edge = heapq.heappop(pq)
			#index = 


		return [mst, cost]

	def fast_prim(self):
		mst = []
		n = len(self.__matrix)-1


		return mst

	def minor(self):
		minor = self.__matrix[0][0]
		for c in self.__matrix[1:]:
			if c[0][1] < minor[1]:
				minor = c[0]
		return minor

	def __addEdges(self, index):
		pass