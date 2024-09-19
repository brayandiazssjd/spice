from CityController import CityController
from Edge import Edge

from disjoint_set import DisjointSet
import heapq

class Controller:

	def __init__(self, ct: CityController):
		self.__matrix = ct.adjmatrix()
		self.__ct = ct

	# Greedy Best-First Search
	def enruteA(self, start, goal):
		adj_matrix = self.__matrix
		n = 30  
		min_heap = [(0, start)]  # (cost, node)
		visited = [False] * n 
		came_from = [-1] * n 
		
		while min_heap:
			current_cost, current_node = heapq.heappop(min_heap)
			if visited[current_node]:
				continue
			# Mark the current node as visited
			visited[current_node] = True
			# If we have reached the goal, we can reconstruct the path
			if current_node == goal:
				return self.reconstruct_path(came_from, start, goal), current_cost
			# Explore neighbors
			for edge in adj_matrix[current_node]:
				if not visited[edge.to]:
					heapq.heappush(min_heap, (edge.cost, edge.to))
					came_from[edge.to] = current_node
		
		# If we exhaust the heap without finding a path, return None
		return None, float('inf')

	# Function to reconstruct the path from start to goal
	def reconstruct_path(self, came_from, start, goal):
		path = []
		current = goal
		while current != start:
			path.append(current)
			current = came_from[current]
		path.append(start)
		path.reverse()
		return path

	def enruteAA(self, start, goal):
		adj_matrix = self.__matrix
		n = 30	
		min_heap = [(0, start)]  # (edge cost + heuristic distance, node)
		visited = [False] * n  # To track visited nodes
		came_from = [-1] * n  # To reconstruct the path

		while min_heap:
			current_priority, current_node = heapq.heappop(min_heap)
			if visited[current_node]:
				continue
			visited[current_node] = True
			if current_node == goal:
				return self.reconstruct_path(came_from, start, goal), current_priority
			for edge in adj_matrix[current_node]:
				neighbor = edge.to
				edge_cost = edge.cost

				if not visited[neighbor]:
					heuristic_to_goal = self.__ct.idistance(neighbor, goal)
					priority = edge_cost + heuristic_to_goal
					# Record the path and push the neighbor to the heap
					came_from[neighbor] = current_node
					heapq.heappush(min_heap, (priority, neighbor))

		# If the goal was not reached, return None
		return None, float('inf')

	def prims_mst(self):
		n = len(self.__matrix)  
		adj_matrix = self.__matrix
		mst_adj_matrix = [[] for _ in range(n)]
		total_cost = 0 
		min_heap = []
		visited = [False] * n  # To track visited cities
		visited[0] = True
		# Añadir todas las aristas desde el nodo 0
		for edge in adj_matrix[0]:
			heapq.heappush(min_heap, (edge.cost, 0, edge.to))  # (cost, from_node, to_node)
		
		while min_heap:
			cost, u, v = heapq.heappop(min_heap)
			if visited[v]:
				continue
			visited[v] = True
			# Aquí creamos el objeto Edge correctamente
			mst_adj_matrix[u].append(Edge(v, cost))
			mst_adj_matrix[v].append(Edge(u, cost))  # El grafo es no dirigido
			total_cost += cost
			# Añadir las aristas de 'v' al heap
			for edge in adj_matrix[v]:
				if not visited[edge.to]:
					heapq.heappush(min_heap, (edge.cost, v, edge.to))
		
		return mst_adj_matrix, total_cost
		# Kruskal's Algorithm for Minimum Spanning Tree
	def kruskal_mst(self):
		adj_matrix = self.__matrix
		n = 30 
		edges = []
		for city_id, neighbors in enumerate(adj_matrix):
			for edge in neighbors:
				edges.append((edge.cost, city_id, edge.to)) 
		edges.sort()
		ds = DisjointSet()
		mst_adj_matrix = [[] for _ in range(n)]
		total_cost = 0 
		for cost, u, v in edges:
			if not ds.connected(u, v):
				ds.union(u, v)
				# Crear correctamente el objeto Edge
				mst_adj_matrix[u].append(Edge(v, cost))
				mst_adj_matrix[v].append(Edge(u, cost)) 
				total_cost += cost
		return mst_adj_matrix, total_cost