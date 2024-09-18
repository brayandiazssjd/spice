from CityController import CityController

import disjoint_set
import heapq

class Controller:

	def __init__(self, ct: CityController):
		self.__matrix = ct.adjmatrix()
		self.__ct = ct

	# Returna el par solución para A
	def enruteA(self, origin: int, destiny: int): 
		dis = 0
		visited = [False for i in range(30)]
		visited[origin] = True
		ids = [origin]
 		
		k = 0
		while origin != destiny and k < 20:
			k+=1
			
			for edge in self.__matrix[origin]:
				if edge.to == destiny:
					return [ids, dis]
				if not visited[edge.to]:
					ids.append(edge.to)
					visited[edge.to] = True
					dis += edge.cost
					origin = edge.to
					break

		ids.append(destiny)
		return [ids, dis]

	def enruteAA(self, origin: int, destiny: int):
		ids = [origin]
		visited = [False for i in range(30)]
		visited[origin] = True
		dis = 0
		k = 0
		while origin != destiny and k < 10:
			k+= 1
			edge = self.__matrix[origin][0]

			nearer = [edge,	self.__ct.idistance(edge.to, destiny)]

			for edge in self.__matrix[1:][origin]:
				distance = self.__ct.idistance(edge.to, destiny)
				if not visited[edge.to]:
					visited[edge.to] = True
					if (distance + edge.cost) < nearer[0].cost + nearer[1]:
						nearer = [edge, distance]
			origin = nearer[0].to
			ids.append(nearer[0].to)
			dis += nearer[0].cost
			
		return [ids, dis] 


	def prims_mst(self):
		n = len(self.__matrix)  
		adj_matrix = self.__matrix
        
		mst = []  
		visited = [False] * n  
		min_heap = [[0, 0]]  

		total_cost = 0  
        
		while len(mst) < n - 1:
			weight, city_id = heapq.heappop(min_heap)
			if visited[city_id]:
				continue
           
			visited[city_id] = True
			total_cost += weight
			if weight != 0: 
				mst.append((city_id, weight))
			for edge in adj_matrix[city_id]:
				neigh_id, edge_cost = edge.to, edge.cost
				if not visited[neigh_id]:
					heapq.heappush(min_heap, [edge_cost, neigh_id])
		return mst, total_cost

	"""def kruskal_mast(self):
		n = len(self.cities)  # Number of cities (nodes)
		adj_matrix = self.adjmatrix()

		# List to store all edges in the graph
		edges = []
		for city_id, neighbors in enumerate(adj_matrix):
			for edge in neighbors:
				edges.append((edge.cost, city_id, edge.to))
        
        # Sort edges by cost (weight)
				edges.sort()

				# Initialize disjoint set for cycle detection
		ds = DisjointSet(n)

				mst = []  # Store edges in the MST
				total_cost = 0  # To store the total cost of the MST

			for cost, u, v in edges:
      # Check if u and v are in different sets to avoid cycles
				if ds.find(u) != ds.find(v):
                ds.union(u, v)
                mst.append((u, v, cost))
                total_cost += cost
            
            # Stop if we have n - 1 edges (MST for a connected graph)
            if len(mst) == n - 1:
                break

        return mst, total_cost"""