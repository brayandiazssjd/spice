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
        passed = []
        while origin != destine:
            # TODO: eliminar este condicional, no es necesario
            if not self.__matrix[origin]:  # Verifica si la lista es vacía o None
                print(f"Error: No hay vecinos disponibles para la ciudad con id {origin}.")
                return route

            for neigh in self.__matrix[origin]:
                if neigh[0] not in passed:  # or neigh[0] == origin
                    route.append(neigh)
                    passed.insert(0, neigh[0])
                    origin = neigh[0]
                    break
        return route

    def enruteAA(self, origin: int, destiny: int):
        route = [[origin, 0]]
        passed = [origin]
        while origin != destiny:
            nearer = [self.__matrix[origin][0][0], self.__ct.idistance(self.__matrix[origin][0][0], destiny), self.__matrix[origin][0][1]]
            for i in range(1, len(self.__matrix[origin])):
                neigh = self.__matrix[origin][i]
                print("$",neigh[0] not in passed)
                distance = self.__ct.idistance(neigh[0], destiny)
                if neigh[0] not in passed:
                    passed.insert(0, neigh[0])
                    
                    if (distance + neigh[1]) < nearer[1] + nearer[2]:
                        nearer = [neigh[0], distance, neigh[1]]
                
            origin = nearer[0]
            route.append([nearer[0], nearer[2]])
            print(passed)
        return route