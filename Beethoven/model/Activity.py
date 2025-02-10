

from typing import Optional


class Activity:

    def __init__(self, id = None, local_noise = None, name = None, start = None, end = None, external_noise = None):
        self.id: Optional[int] = id
        self.name: Optional[str] = name
        self.start: Optional[int] = start
        self.end: Optional[int] = end
        self.external_noise: Optional[int] = external_noise
        self.local_noise: Optional[int] = local_noise

    
    def __str__(self) -> str:
        return f"(id={self.id}, name={self.name}, local_noise={self.local_noise}, start={self.start}, end={self.end}, max_noise={self.external_noise})"
