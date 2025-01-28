from Sound import Sound
from Time import Time

class Activity:

    def __init__(self, name: str, sound: Sound, start: Time, end:Time):
        self.name = name
        self.sound = sound
        self.start = start
        self.end = end

    def getImpact(self) -> float:
        pass