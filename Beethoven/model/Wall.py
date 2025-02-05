from typing import List, Optional
from Material import Material

class Wall:

    def __init__(self, id: int, isolation_rating: int):
        self.id = id
        #self.materials: Optional[List[Material]] = materials
        self.isolation_rating = isolation_rating
