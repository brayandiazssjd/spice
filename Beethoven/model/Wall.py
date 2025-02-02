from typing import List
from Material import Material

class Wall:

    def __init__(self, id: int, materials: List[Material]):
        self.id = id
        self.materials = materials
