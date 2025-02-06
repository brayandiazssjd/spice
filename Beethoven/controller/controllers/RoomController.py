import json
###
from model.Activity import Activity
###
from model.Graph import Graph
from ..factories.RoomFactory import RoomFactory
from model.Room import Room
from model.Wall import Wall
from .Controller import Controller
from typing import List
from model.Node import Node


class RoomController:

    def __init__(self):
        self.rooms: list[Room] = []
        # TESTEO P
        self.activities = [  # Lista de actividades (la misma que proporcionaste)
            {"id": 0, "name": "Educación física", "external_noise": 40, "local_noise": 50, "start": 8, "end": 10},
            {"id": 1, "name": "Baile", "external_noise": 50, "local_noise": 60, "start": 8, "end": 10},
            {"id": 2, "name": "Yoga", "external_noise": 30, "local_noise": 20, "start": 8, "end": 10},
            {"id": 3, "name": "Cátedra", "external_noise": 20, "local_noise": 30, "start": 8, "end": 10},
            {"id": 4, "name": "Conferencia", "external_noise": 25, "local_noise": 35, "start": 8, "end": 10},
            {"id": 5, "name": "Debate", "external_noise": 35, "local_noise": 55, "start": 8, "end": 10},
            {"id": 6, "name": "Laboratorio", "external_noise": 15, "local_noise": 25, "start": 8, "end": 10},
            {"id": 7, "name": "Investigación", "external_noise": 20, "local_noise": 20, "start": 8, "end": 10},
            {"id": 8, "name": "Teatro", "external_noise": 35, "local_noise": 45, "start": 8, "end": 10}
        ]
        self.create_test_rooms()

    def create_test_rooms(self):
        # Crea las rooms
        room0 = Room(0)
        room1 = Room(1)
        room2 = Room(2)
        room3 = Room(3)
        room4 = Room(4)
        room5 = Room(5)
        room6 = Room(6)
        room7 = Room(7)
        room8 = Room(8)
        room9 = Room(9)

        # Crea Walls de prueba
        wall_0_1 = Wall(0, 2)  # Wall id 0, isolation 2
        wall_0_2 = Wall(1, 3)  # Wall id 1, isolation 3
        wall_1_3 = Wall(2, 4)  # Wall id 2, isolation 4
        wall_1_4 = Wall(3, 1)  # Wall id 3, isolation 1
        wall_2_5 = Wall(4, 2)  # Wall id 4, isolation 2
        wall_2_6 = Wall(5, 3)  # Wall id 5, isolation 3
        wall_3_7 = Wall(6, 4)  # Wall id 6, isolation 4
        wall_3_8 = Wall(7, 1)  # Wall id 7, isolation 1
        wall_4_9 = Wall(8, 2)  # Wall id 8, isolation 2
        wall_4_5 = Wall(9, 3)  # Wall id 9, isolation 3
        wall_5_6 = Wall(10, 4)  # Wall id 10, isolation 4
        wall_6_7 = Wall(11, 1)  # Wall id 11, isolation 1
        wall_7_8 = Wall(12, 2)  # Wall id 12, isolation 2
        wall_8_9 = Wall(13, 3)  # Wall id 13, isolation 3

        # Define las relaciones (¡usando objetos Room y Wall!)
        room0.relations = [(room1, wall_0_1), (room2, wall_0_2)]
        room1.relations = [(room0, wall_0_1), (room3, wall_1_3), (room4, wall_1_4)]
        room2.relations = [(room0, wall_0_2), (room5, wall_2_5), (room6, wall_2_6)]
        room3.relations = [(room1, wall_1_3), (room7, wall_3_7), (room8, wall_3_8)]
        room4.relations = [(room1, wall_1_4), (room9, wall_4_9), (room5, wall_4_5)]
        room5.relations = [(room2, wall_2_5), (room4, wall_4_5), (room6, wall_5_6)]
        room6.relations = [(room2, wall_2_6), (room5, wall_5_6), (room7, wall_6_7)]
        room7.relations = [(room3, wall_3_7), (room6, wall_6_7), (room8, wall_7_8)]
        room8.relations = [(room3, wall_3_8), (room7, wall_7_8), (room9, wall_8_9)]
        room9.relations = [(room4, wall_4_9), (room8, wall_8_9)]

        # Asigna actividades a las rooms (una actividad por room)
        for i, room in enumerate(self.rooms):
            activity_index = i % len(self.activities)  # Distribuye las actividades cíclicamente
            activity_data = self.activities[activity_index]
            activity = Activity(activity_data["id"], activity_data["name"], activity_data["external_noise"], activity_data["local_noise"], activity_data["start"], activity_data["end"])
            room.activities = [activity]  # Asigna la actividad a la room (en una lista)
            
        self.rooms = [room0, room1, room2, room3, room4, room5, room6, room7, room8, room9]
    # FIN DEL TESTEO P MANO

    def upload(self, source: str, walls: List[Wall]):
        with open(source, "r") as file:
            data_list = json.load(file)
        f = RoomFactory()
        self.rooms = [f.create(data) for data in data_list]
        for room in self.rooms:
            room.relations = [(self.rooms[relation['room']], walls[relation['wall']]) for relation in data_list[room.id]['relations']]

    def getHabitability(self):
        pass

    def get_graph(self) -> Graph:
        nodes: List[Node] = []
        for room in self.rooms:
            nodes.append(Node(room.id, room)) # Guarda el objeto Room en el Nodo

        for node in nodes:
            for nbr_room, wall in node.room.relations: # Accede a room.relations
                node.add_edge(nbr_room.id, wall.isolation_rating) # Usa la relacion para crear la arista
        return Graph(nodes)

    """def get_graph(self) -> Graph:
        nodes: List[Node] = [Node(i, i) for i in range(len(self.rooms))]
        for node in nodes:
            node.edges = [(nbr.id, nbr.activity-wall.isolation_rating) for nbr, wall in self.rooms[node.room].relations]
        return Graph(nodes) """
