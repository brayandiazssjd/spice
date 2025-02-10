import json
import random
from model.Activity import Activity
from model.Graph import Graph
import os
from ..factories.RoomFactory import RoomFactory
from model.Room import Room
from model.Wall import Wall
from .Controller import Controller
from typing import List, Tuple
from model.Node import Node


class RoomController:

    def __init__(self):
        self.rooms: list[Room] = []
        self.walls: list[Wall] = []
        self.activities = [
            {"id": 0, "name": "Educación física", "external_noise": 40, "local_noise": 45, "start": 8, "end": 10},
            {"id": 1, "name": "Baile", "external_noise": 50, "local_noise": 55, "start": 8, "end": 10},
            {"id": 2, "name": "Yoga", "external_noise": 30, "local_noise": 20, "start": 8, "end": 10},
            {"id": 3, "name": "Cátedra", "external_noise": 35, "local_noise": 25, "start": 8, "end": 10},
            {"id": 4, "name": "Conferencia", "external_noise": 35, "local_noise": 30, "start": 8, "end": 10},
            {"id": 5, "name": "Debate", "external_noise": 35, "local_noise": 40, "start": 8, "end": 10},
            {"id": 6, "name": "Laboratorio", "external_noise": 20, "local_noise": 20, "start": 8, "end": 10},
            {"id": 7, "name": "Investigación", "external_noise": 20, "local_noise": 20, "start": 8, "end": 10},
            {"id": 8, "name": "Teatro", "external_noise": 35, "local_noise": 40, "start": 8, "end": 10}
        ]
        self.create_test_rooms()

    def create_test_rooms(self):

        # Crea las rooms
        for i in range (20):
            self.rooms.append(Room(i))

        # Crea las walls
        for i in range (36):
            isolation = random.randint(1,4)
            self.walls.append(Wall(i, isolation))

        # Crea las relaciones
        for i in range(5):
            for j in range(0, 20, 4):
                self.rooms[j].relations = [(self.rooms[j+1], self.walls[j]), (self.rooms[j+2], self.walls[j+1])]
                self.rooms[j+1].relations = [(self.rooms[j], self.walls[j]), (self.rooms[j+3], self.walls[j+2])]
                self.rooms[j+2].relations = [(self.rooms[j], self.walls[j+1]), (self.rooms[j+3], self.walls[j+3])]
                self.rooms[j+3].relations = [(self.rooms[j+1], self.walls[j+2]), (self.rooms[j+3], self.walls[j+3])]
                if (j+4 < len(self.rooms)):
                    self.rooms[j].relations.append((self.rooms[j+4], self.walls[j+4]))
                    self.rooms[j+1].relations.append((self.rooms[j+5], self.walls[j+5]))
                    self.rooms[j+2].relations.append((self.rooms[j+6], self.walls[j+6]))
                    self.rooms[j+3].relations.append((self.rooms[j+7], self.walls[j+7]))

        # Asigna actividades a las rooms (una actividad por room)
        for i, room in enumerate(self.rooms):
            if(i<16):
                activity_index = i % len(self.activities)  # Distribuye las actividades cíclicamente
                activity_data = self.activities[activity_index]
                activity = Activity(activity_data["id"], name=activity_data["name"], external_noise=activity_data["external_noise"], local_noise=activity_data["local_noise"], start=activity_data["start"], end=activity_data["end"])
                room.activities = [activity]
            else:
                activity_none = Activity(id=-1,local_noise=0 ,name="none", start=0, end=0, external_noise=0)
                room.activities = [activity_none]

    def upload(self, source: str, walls: List[Wall]):
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..","data", source))
        with open(path, "r") as file:
            data_list = json.load(file)
        f = RoomFactory()
        self.rooms = [f.create(data) for data in data_list]
        for room in self.rooms:
            room.relations = [(self.rooms[relation['room']], walls[relation['wall']]) for relation in data_list[room.id]['relations']]

    def getHabitability(self):
        pass

    def get_graph(self) -> Tuple[Graph, dict]:
        nodes: List[Node] = []
        node_dict = {}

        for room in self.rooms:
            node = Node(room.id, room)
            nodes.append(node)
            node_dict[room.id] = node

        for node in nodes:
            for nbr_room, wall in node.room.relations:
                node.add_edge(nbr_room.id, wall.isolation_rating)

        for node in nodes:
            node.edges = [(nbr.id, nbr.activities[0].local_noise - wall.isolation_rating) for nbr, wall in node.room.relations]

            if(node.room.activities[0].id==-1):
                node.color = -1
                break
            node.color = 0
            for _, weight in node.edges:
                external_noise = node.room.activities[0].external_noise
                if (external_noise + 10) > weight and weight > external_noise:
                    node.color = 1
                elif (external_noise + 15) > weight and weight > (external_noise + 10):
                    node.color = 3
                elif weight > external_noise:
                    node.color = 2

        return Graph(nodes), node_dict
