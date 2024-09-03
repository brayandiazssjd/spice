import math


class Controller:

  def __init__(self, matrix):
    self.matrix = matrix

  

  """
  #Recursivo
  def enrute(self, origin, destine, visited):
      if origin == destine:
          return [destine]
      next_one = self.__next(origin, destine, visited)

      return [origin] + self.enrute(next_one,destine, visited.append(origin))

  def __next(self, origin, destine, visited):
      for neigh in self.matrix[origin]:
          if neigh[0] not in visited or neigh[0] == destine:
              return neigh
      return -1
  """

  def enruteA(self, origin, destine):
    route = []

    while origin != destine:
      for neigh in self.matrix[origin]:
        if neigh not in route: # or neigh[0] == origin
          route.append(neigh)
          origin = neigh[0]
          break
    return route

  def enruteAA(self, origin, destine):
    route = []
    passed = []
    while origin != destine:
      nearer = None
      for neigh in self.matrix[origin]:
        if neigh[0] not in passed and self.distance(neigh[]):
          nearer = neigh
          passed.append(neigh[0])
      origin = nearer
      route.append(nearer)
    return route

