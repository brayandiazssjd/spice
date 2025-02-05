import json
from ..factories.RoomFactory import RoomFactory
from model.Room import Room
from model.Wall import Wall
from .Controller import Controller
from typing import List


class RoomController:

    def __init__(self):
        self.rooms = []

    def upload(self, source: str, walls: List[Wall]):
        with open(source, "r") as file:
            data_list = json.load(file)
        f = RoomFactory()
        self.rooms = [f.create(data) for data in data_list]
        for room in self.rooms:
            room.relations = [(self.rooms[relation['room']], walls[relation['wall']]) for relation in data_list[room.id]['relations']]

    def getHabitability(self):
        pass
