from typing import Callable, Dict, List, Optional
import json

from Beethoven.controller.Factory import Factory


class Controller[T]:
    
    def __init__(self):
        self.objects: List[T] = []

    def get(self, f: Callable[[T], bool]) -> Optional[T]:
        for obj in self.objects:
            if f(obj):
                return obj
        return None

    def add(self, T):
        self.objects.append(T)


    def upload(self, source: str, factory: Factory) -> None:
        with open(source, "r") as file:
            data_list = json.load(file)
        self.objects = [factory.create(data) for data in data_list]
