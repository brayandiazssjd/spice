from typing import Set, Tuple


class RadioStation:
    def __init__(self, id: int, name: str) -> None:
        self.color = ""
        self.id = id
        self.name = name
        self.neighbors: Set[Tuple[RadioStation, int]] = set() # Almacena las tuplas (neighbour, distance)
        
    # Return the number of neightbours.
    @property
    def degree(self) -> int:
        return len(self.neighbors)
