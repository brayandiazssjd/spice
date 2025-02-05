from Beethoven.controller.factories.Factory import Factory
from model.Wall import Wall
from typing import Dict


class WallFactory(Factory[Wall]):
    def __init__(self) -> None:
        super().__init__()

    def create(self, data: Dict) -> Wall:
        return Wall(data['id'], data['isolation_rate'])
