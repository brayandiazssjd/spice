from abc import ABC, abstractmethod

class Weightable(ABC):
    @abstractmethod
    def weight(self, id):
        pass
