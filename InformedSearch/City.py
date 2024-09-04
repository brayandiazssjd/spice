

class City:
  def __init__(self, lat, lon, name) -> None:
    self.name = name
    self.lat = lat
    self.lon = lon

  @property
  def neighs(self):
      return self.__neighs

  @neighs.setter
  def neighs(self, value):
      self.__neighs = value
