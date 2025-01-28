from Wall import Wall
from Room import Room

class Relation:

    def __init__(self, wall: Wall, neigh: Room):
        self.wall = wall
        self.neigh = neigh