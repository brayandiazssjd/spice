from CityController import CityController


class Controller:

    def __init__(self, matrix, ct: CityController):
        self.__matrix = matrix
        self.__ct = ct

        """
        #Recursiv
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
            if not self.__matrix[origin]:  # Verifica si la lista es vacía o None
                print(f"Error: No hay vecinos disponibles para la ciudad con id {origin}.")
                return route

            for neigh in self.__matrix[origin]:
                if neigh[0] not in route:  # or neigh[0] == origin
                    route.append(neigh[0])
                    origin = neigh[0]
                    break
        return route

    def enruteAA(self, origin: int, destiny: int):
        route = []
        passed = []
        while origin != destiny:
            nearer = [destiny, self.__ct.idistance(origin, destiny)]
            for neigh in self.__matrix[origin]:
                distance = self.__ct.idistance(origin, neigh[0]) + neigh[1]
                if neigh[0] not in passed and distance > nearer[1]:
                    nearer = [neigh[0], distance]
                    passed.insert(0, neigh[0])
                origin = nearer[0]
                route.append(nearer[0])
        return route 
