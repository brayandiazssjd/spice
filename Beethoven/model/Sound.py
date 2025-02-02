class Sound:

    def __init__(self, frecuency: float, pressure: float):
        self.frecuency = frecuency
        self.pressure = pressure

    def getNoise(self) -> float:
        return self.frecuency*self.pressure
