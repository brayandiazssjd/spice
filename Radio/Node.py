

class Node:
    def __init__(self, id: int, name: str) -> None:
        self.color: str = ""
        self.id: int = id
        self.name = name
        self.neights: list = [] # Almacena las tuplas (neigh pointer, distance)
        
    # Return the number of neightbours.
    @property
    def count(self) -> int:
        return len(self.neights)

	# distance is (pointer, distance) 
    def add(self, distance):
        self.neights.append(distance)

