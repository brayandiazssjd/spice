import json
from Beethoven.controller.factories.RoomFactory import RoomFactory
from Beethoven.model.Room import Room
from Beethoven.model.Wall import Wall
from Controller import Controller


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