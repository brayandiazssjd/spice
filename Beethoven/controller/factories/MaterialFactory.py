from typing import Dict
from .Factory import Factory
from model.Material import Material


class MaterialFactory(Factory[Material]):
    def __init__(self) -> None:
        pass

    def create(self, data: Dict) -> Material:
        return Material(data['id'], data['name'], data['isolation_rate'])
