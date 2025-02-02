class Time:

    def __init__(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute

    def __str__(self) -> str:
        return f"Time (hour={self.hour}, minute={self.minute})"
