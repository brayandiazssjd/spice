

class City:
    def __init__(self, id: int, lat, lon, name) -> None:
        self.name = name
        self.lat = lat
        self.lon = lon
        self.id: int = id

    @property
    def neighs(self):
        return self.__neighs

    @neighs.setter
    def neighs(self, value):
        self.__neighs = value

    def tostr(self):
        n = ", neighs=["
        for neigh in self.__neighs:
            n += neigh.name +","
        n += "]"
        return "City (lat="+str(self.lat)+", lon="+str(self.lon)+", name="+self.name+n

