from typing import TypeVar, Generic, List, Optional, Any

T = TypeVar("T")

class Controller(Generic[T]):
    
    def __init__(self):
        self.objects: List[T] = []

    def create(self):
        pass