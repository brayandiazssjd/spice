from Sound import Sound
from Time import Time


class Activity:

    def __init__(self, name: str, sound: Sound, start: Time, end:Time, max_noise: int):
        self.name = name
        self.sound = sound
        self.start = start
        self.end = end
        self.max_noise = max_noise

    def __str__(self) -> str:
        return f"(name={self.name}, sound={self.sound}, start={self.start}, end={self.end}, max_noise={self.max_noise})"
