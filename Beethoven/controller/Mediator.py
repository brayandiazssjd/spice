import random
from model.Node import Node
from controller.controllers.ActivityController import ActivityController
from controller.controllers.MaterialController import MaterialController
from controller.controllers.WallController import WallController
from controller.controllers.RoomController import RoomController
from controller.factories.MaterialFactory import MaterialFactory
from controller.factories.WallFactory import WallFactory
from controller.factories.ActivityFactory import ActivityFactory
from controller.factories.RoomFactory import RoomFactory
from model.Graph import Graph

class Mediator:

    def __init__(self):
        self.room_controller: RoomController = RoomController()
        self.wall_controller: WallController = WallController()
        self.material_controller: MaterialController = MaterialController()
        self.activity_controller: ActivityController = ActivityController()
        
        
        #self.room_controller.upload("Beethoven/data/rooms.json", RoomFactory())
        #self.activity_controller.upload("Beethoven/data/activities.json", ActivityFactory())
        #self.wall_controller.upload("Beethoven/data/walls.json", WallFactory())
        #self.material_controller.upload("Beethoven/data/material.json", MaterialFactory())   

    def cambiarAct(self, act, idRoom):
        # Buscar la habitación por su ID
        idRoom = int(idRoom)
        room = next((room for room in self.room_controller.rooms if room.id == idRoom), None)
        
        if room:
            # Si la habitación existe, actualiza su lista de actividades
            if room.activities is None:
                room.activities = []  # Inicializa la lista si está vacía
            
        # Elimina la actividad anterior (si hay alguna)
        if room.activities:
            room.activities.pop()  # Elimina el último elemento de la lista (puedes ajustar esto si necesitas eliminar una actividad específica)

            # Añade la nueva actividad
            room.activities.append(act)
            print(f"Actividad '{act}' reemplazada en la habitación con ID {idRoom}.")
        else:
            print(f"Habitación con ID {idRoom} no encontrada.")

    def getInfo(self, id):
        id = int(id)
        room = next((room for room in self.room_controller.rooms if room.id == id), None)
        act = room.activities
        return act
    
    def get_graph_data(self):
        graph = self.room_controller.get_graph()
        nodes_data = {}
        edges_data = {}

        for node_id, node in graph.nodes.items():
            nodes_data[node_id] = node.room # Guarda el objeto Room en el diccionario
            edges_data[node_id] = [(neighbor, weight) for neighbor, weight in node.edges]

        return {'nodes': nodes_data, 'edges': edges_data}