from CityController import CityController

import disjoint_set
import heapq

class Controller:

	def __init__(self, ct: CityController):
		self.__matrix = ct.adjmatrix()
		self.__ct = ct

	# Returna el par solución para A
	"""def enruteA(self, origin: int, destiny: int): 
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
		return [ids, dis]"""
	
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

	"""def enruteAA(self, origin: int, destiny: int):
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
			
		return [ids, dis] """
	
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

		# Create an empty MST adjacency matrix
		mst_adj_matrix = [[] for _ in range(n)]
		total_cost = 0  # Total cost of the MST

		# Min-heap (priority queue) for selecting the minimum cost edge
		min_heap = []
		visited = [False] * n  # To track visited cities

		# Start with city 0 (arbitrary choice)
		visited[0] = True
		for edge in adj_matrix[0]:
			heapq.heappush(min_heap, (edge.cost, 0, edge.to))  # (cost, from_node, to_node)

		while min_heap:
			cost, u, v = heapq.heappop(min_heap)

			# If the destination node v has already been visited, skip this edge
			if visited[v]:
				continue

			# Mark the destination node as visited
			visited[v] = True

			# Add the edge to the MST adjacency matrix
			mst_adj_matrix[u].append(edge(v, cost))  # Use the Edge class to create an Edge object
			mst_adj_matrix[v].append(edge(u, cost))  # Since the graph is undirected
			total_cost += cost

			# Explore the neighbors of the newly added node v
			for edge in adj_matrix[v]:
				if not visited[edge.to]:
					heapq.heappush(min_heap, (edge.cost, v, edge.to))

		return mst_adj_matrix, total_cost

	
	# Kruskal's Algorithm for Minimum Spanning Tree
	def kruskal_mst(self):
		adj_matrix = self.__matrix
		n = 30  # Number of cities (nodes)
		
		# Prepare the list of all edges
		edges = []
		for city_id, neighbors in enumerate(adj_matrix):
			for edge in neighbors:
				edges.append((edge.cost, city_id, edge.to))  # (cost, from_node, to_node)

		# Sort edges by cost (ascending)
		edges.sort()

		# Initialize DisjointSet to manage connected components
		ds = disjoint_set.DisjointSet()

		# Create a new adjacency matrix for the MST
		mst_adj_matrix = [[] for _ in range(n)]
		total_cost = 0  # Total cost of the MST

		for cost, u, v in edges:
			# Check if u and v are in the same set (component)
			if not ds.connected(u, v):
				# If they are not connected, include this edge in the MST
				ds.union(u, v)
				# Add the edge to the MST adjacency matrix for both u and v
				mst_adj_matrix[u].append(edge(v, cost))
				mst_adj_matrix[v].append(edge(u, cost))  # Since the graph is undirected
				total_cost += cost

		return mst_adj_matrix, total_cost

	"""def prims_mst(self):
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
		return mst, total_cost"""

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