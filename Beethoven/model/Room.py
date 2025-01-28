from Relation import Relation
from Activity import Activity
from typing import List

class Room:
    def __init__(self, id: int, habitable: bool, relations: List[Relation], activities: List[Activity]):
        self.id = id
        self.habitable = habitable
        self.relations = relations
        self.activities = activities