from abc import ABC, abstractmethod
from typing import Dict


class Factory[T](ABC):
    @abstractmethod
    def create(self, data: Dict) -> T:
        pass
