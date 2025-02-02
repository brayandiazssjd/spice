from abc import ABC, abstractmethod
from typing import Callable, Optional

class Controller[T](ABC):
    
    def __init__(self):
        self.objects: list[T] = []

    def get(self, f: Callable[[T], bool]) -> Optional[T]:
        for obj in self.objects:
            if f(obj):
                return obj
        return None

    def add(self, T):
        self.objects.append(T)

    @abstractmethod
    def upload(self) -> None:
        pass
