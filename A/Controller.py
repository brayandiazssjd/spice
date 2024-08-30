class Controller:
    def __init__(self, matrix):
        self.matrix = matrix

    def distance(self, origin, destine):
        pass

    """
    # Retorna una lista con id de las ciudades que son parte del camino
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
    def enrute(self, origin, destine):
        route = []
    
        while origin != destine:
            for neigh in self.matrix[origin]:
                if neigh[0] not in route or neigh[0] != origin:
                    route.append(neigh[0])
                    origin = neigh
                    break
        return route
