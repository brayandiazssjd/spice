from Beethoven.controller.controllers.ActivityController import ActivityController
from Beethoven.controller.controllers.MaterialController import MaterialController
from Beethoven.controller.controllers.WallController import WallController
from Beethoven.controller.controllers.RoomController import RoomController
from Beethoven.controller.factories.MaterialFactory import MaterialFactory
from Beethoven.controller.factories.WallFactory import WallFactory
from Beethoven.controller.factories.ActivityFactory import ActivityFactory
from Beethoven.controller.factories.RoomFactory import RoomFactory
from Window import Window


class Mediator:

    def __init__(self):
        self.room_controller: RoomController = RoomController()
        self.wall_controller: WallController = WallController()
        self.material_controller: MaterialController = MaterialController()
        self.activity_controller: ActivityController = ActivityController()
        self.window = Window(self)
        
        
        self.room_controller.upload("Beethoven/data/rooms.json", RoomFactory())
        self.activity_controller.upload("Beethoven/data/activities", ActivityFactory())
        self.wall_controller.upload("Beethoven/data/walls.json", WallFactory())
        self.material_controller.upload("Beethoven/data/material.json", MaterialFactory())   

def cambiarAct(self, act, idRoom):
    # Buscar la habitación por su ID
    room = next((room for room in self.room_controller.rooms if room.id == idRoom), None)
    
    if room:
        # Si la habitación existe, actualiza su lista de actividades
        if room.activities is None:
            room.activities = []  # Inicializa la lista si está vacía
        
        room.activities.append(act)  # Añade la nueva actividad
        print(f"Actividad '{act}' añadida a la habitación con ID {idRoom}.")
    else:
        print(f"Habitación con ID {idRoom} no encontrada.")
