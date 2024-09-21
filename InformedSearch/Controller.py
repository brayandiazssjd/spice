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
	
	def dijkstra(self, start, goal):
		adj_matrix = self.__matrix  
		n = len(adj_matrix)  
		min_heap = [(0, start)]  # Cola de prioridad mínima (costo, nodo)
		distances = [float('inf')] * n  # Inicializar distancias a infinito
		distances[start] = 0  # La distancia al nodo de inicio es 0
		came_from = [-1] * n  # Para reconstruir el camino
		visited = [False] * n  # Para rastrear nodos visitados

		while min_heap:
			current_cost, current_node = heapq.heappop(min_heap)  # Extraer el nodo con el menor costo
			if visited[current_node]:
				continue  # Si ya fue visitado, continuar con el siguiente
			visited[current_node] = True  # Marcar el nodo como visitado

			if current_node == goal:
				# Si llegamos al nodo objetivo, reconstruir y devolver el camino y el costo
				return self.reconstruct_path(came_from, start, goal), current_cost

			for edge in adj_matrix[current_node]:
				neighbor = edge.to  # Nodo vecino
				new_cost = current_cost + edge.cost  # Calcular el nuevo costo

				if new_cost < distances[neighbor]:
					# Si encontramos un camino más corto al vecino, actualizar la distancia
					distances[neighbor] = new_cost
					came_from[neighbor] = current_node  # Registrar de dónde venimos
					heapq.heappush(min_heap, (new_cost, neighbor))  # Añadir el vecino a la cola de prioridad

		# Si no encontramos un camino al nodo objetivo, devolver None y costo infinito
		return None, float('inf')
	
	
	def bellman(self, start, goal):
		adj_matrix = self.__matrix
		n = len(adj_matrix)  

		# Inicializar las distancias de todos los nodos a infinito (excepto el nodo de inicio)
		distances = [float('inf')] * n  # Lista de distancias mínimas desde el nodo de inicio a cada nodo
		came_from = [-1] * n  # Lista que almacena desde qué nodo llegamos al nodo actual
		distances[start] = 0  # La distancia al nodo de inicio es 0

		# Proceso de relajación n - 1 veces (donde n es el número de nodos)
		for _ in range(n - 1):
			# Para cada nodo en el grafo
			for u in range(n):
				# Iterar sobre todas las aristas del nodo actual u
				for edge in adj_matrix[u]:
					v = edge.to  # Nodo adyacente a u
					weight = edge.cost  # Peso de la arista entre u y v

					# Si la distancia a u no es infinita y encontramos una distancia más corta a v
					if distances[u] != float('inf') and distances[u] + weight < distances[v]:
						distances[v] = distances[u] + weight  # Actualizamos la distancia mínima a v
						came_from[v] = u  # Registramos que llegamos a v desde u

					# Considerar la arista en la dirección opuesta (para grafos no dirigidos)
					if distances[v] != float('inf') and distances[v] + weight < distances[u]:
						distances[u] = distances[v] + weight  # Actualizamos la distancia mínima a u
						came_from[u] = v  # Registramos que llegamos a u desde v

		# Después de la relajación, verificamos si hay ciclos de peso negativo
		for u in range(n):
			for edge in adj_matrix[u]:
				v = edge.to  # Nodo adyacente a u
				weight = edge.cost  # Peso de la arista entre u y v

				# Si todavía se puede reducir una distancia, significa que hay un ciclo de peso negativo
				if distances[u] != float('inf') and distances[u] + weight < distances[v]:
					raise ValueError("Graph contains a negative-weight cycle")  # Lanzamos error

				# También comprobamos la dirección opuesta para grafos no dirigidos
				if distances[v] != float('inf') and distances[v] + weight < distances[u]:
					raise ValueError("Graph contains a negative-weight cycle")  # Lanzamos error

		# Si la distancia al nodo de destino es infinita, significa que no hay un camino posible
		if distances[goal] == float('inf'):
			return None, float('inf')

		# Si existe un camino válido, devolvemos el camino reconstruido y la distancia mínima al nodo objetivo
		return self.reconstruct_path(came_from, start, goal), distances[goal]
