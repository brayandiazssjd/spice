from RoomController import RoomController
from view import Window

class Mediator:

    def __init__(self, roomController: RoomController, window: Window):
        self.roomController = roomController
        self.window = window