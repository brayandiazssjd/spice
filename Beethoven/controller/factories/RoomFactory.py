from typing import Dict
from Factory import Factory
from model.Room import Room


class RoomFactory(Factory[Room]):
    def __init__(self) -> None:
        super().__init__()

    def create(self, data: Dict) -> Room:
        room = Room(data['id'])
        return room
