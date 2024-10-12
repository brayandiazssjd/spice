from abc import ABC, abstractmethod

class Sortable(ABC):
    @abstractmethod
    def getId(self):
        pass
