from Activity import Activity
from Wall import Wall
from Room import Room
from typing import List, Optional, Tuple

class Room:
    def __init__(self, id: int, relations = None , activities = None):
        self.id = id
        self.relations: Optional[List[Tuple[Room, Wall]]] = relations
        self.activities: Optional[List[Activity]] = activities
