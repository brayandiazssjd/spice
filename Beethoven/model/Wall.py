from typing import List, Optional
from Material import Material

class Wall:

    def __init__(self, id: int, materials = None):
        self.id = id
        self.materials: Optional[List[Material]] = materials
