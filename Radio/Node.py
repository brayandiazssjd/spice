

class Node:
	def __init__(self, id: int, name: str) -> None:
		self.color = ""
		self.id = id
		self.name= name
		self.neighbors = [] # Almacena las tuplas (neighbour id, distance)
		
	# Return the number of neightbours.
	@property
	def count(self) -> int:
		return len(self.neighbors)

	# distance is (pointer, measure) 
	def add(self, distance):
		self.neighbors.append(distance)
