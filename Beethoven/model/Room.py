from Activity import Activity
from Wall import Wall
from Room import Room
from typing import List, Tuple

class Room:
    def __init__(self, id: int, habitable: bool, relations: List[Tuple[Room, Wall]], activities: List[Activity]):
        self.id = id
        self.habitable = habitable
        self.relations = relations
        self.activities = activities
