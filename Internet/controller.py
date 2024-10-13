from Router import Router
# en terminal: pip install networkx matplotlib
import networkx as nx
import matplotlib.pyplot as plt
from heapq import heapify, heappop, heappush

class Controller:
    def __init__(self):
        self.routers = []  

    def man(self):
        # Asignar valores a routers. La enumeración se puede ver en Internet\RedRouters.png
        id = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        #vel = [100, 98, 96, 94, 92, 90, 88, 86, 83, 84, 82, 80, 78, 76, 74, 72, 102, 204, 306, 408, 150, 250, 350, 450, 820, 840, 860, 880, 900, 920, 940, 960]
        ping = [80, 82, 84, 86, 88, 90, 92, 83, 94, 96, 98, 100, 102, 104, 106, 108, 40, 42, 44, 46, 48, 50, 52, 54, 20, 25, 15, 30, 18, 22, 28, 26]
        names = [
            "Ana", "Ben", "Cara", "Dan", "Eva", "Finn", "Gina", "Hank", "Santiago",
            "Ivy", "Jack", "Kara", "Leo", "Mia", "Nina", "Oscar", 
            "Claro", "Movistar", "Tigo", "T-Mobile", "Sprint", "Cox", "Spectrum", "ETB",
            "AT&T", "Verizon", "CenturyLink", "Frontier", "Windstream", "Mediacom", "Suddenlink", "Optimum"
        ]
        #pylint: disable= too-many-function-args
        self.routers = [Router(id[i], names[i], ping[i]) for i in range(0, 32)]

        #Vecinos 
        r = self.routers

        neighs=[
            [r[1],r[15], r[17]], #0
            [r[0], r[17], r[2]], #1
            [r[1],r[3],r[17]], #2
            [r[2], r[18], r[17]], #3
            [r[18]], #4
            [r[19],r[18]], #5
            [r[7]], #6
            [r[8],r[6],r[20]], #7
            [r[7], r[20]], #8
            [r[22],r[21]], #9
            [r[21]], #10
            [r[22],r[21]], #11
            [r[22]], #12
            [r[23]], #13
            [r[15],r[16]], #14
            [r[0], r[14],r[23],r[16]], #15
            [r[14],r[15],r[17],r[23],r[25]], #16
            [r[0],r[1],r[2],r[3],r[16],r[22],r[26]], #17
            [r[3], r[4], r[5], r[19],r[21],r[23]], #18
            [r[20], r[5],r[18]], #19
            [r[21],r[8], r[7],r[19]], #20
            [r[11],r[10],r[9],r[20],r[18]], #21
            [r[12],r[11],r[9],r[17],r[31]], #22
            [r[15], r[13],r[16],r[18]], #23
            [r[31],r[25],r[26],r[30]], #24
            [r[24],r[26],r[27],r[29],r[16]], #25
            [r[25], r[27],r[24],r[17]], #26
            [r[28],r[26],r[25],r[31]], #27
            [r[29],r[30],r[27]], #28
            [r[28],r[25]], #29
            [r[28],r[31],r[24]], #30
            [r[30],r[24], r[27],r[22]] #31 
        ]

        for i in range(0, 32): #0 a 31
            r[i].table = neighs[i]
        
        for router in self.routers:
            neighbors_ids = [neighbor.id for neighbor in router.table]
            print(f"Router {router.id} ({router.name}): {neighbors_ids}")

    def graph(self):
        # Lista de vecinos
        neighs = [
            [1, 15, 17],  # 0
            [0, 17, 2],   # 1
            [1, 3, 17],   # 2
            [2, 18, 17],  # 3
            [18],         # 4
            [19, 18],     # 5
            [7],          # 6
            [8, 6, 20],   # 7
            [7, 20],      # 8
            [22, 21],     # 9
            [21],         # 10
            [22, 21],     # 11
            [22],         # 12
            [23],         # 13
            [15, 16],     # 14
            [0, 14, 23, 16],  # 15
            [14, 15, 17, 23, 25],  # 16
            [0, 1, 2, 3, 16, 22, 26],  # 17
            [3, 4, 5, 19, 21, 23],  # 18
            [20, 5, 18],  # 19
            [21, 8, 7, 19],  # 20
            [11, 10, 9, 20, 18],  # 21
            [12, 11, 9, 17, 31],  # 22
            [15, 13, 16, 18],  # 23
            [31, 25, 26, 30],  # 24
            [24, 26, 27, 29, 16],  # 25
            [25, 27, 24, 17],  # 26
            [28, 26, 25, 31],  # 27
            [29, 30, 27],  # 28
            [28, 25],      # 29
            [28, 31, 24],  # 30
            [30, 24, 27, 22]   # 31
        ]
        
        # Crear el grafo
        G = nx.Graph()

        # Añadir conexiones entre nodos (aristas)
        for nodo, vecinos in enumerate(neighs):
            for vecino in vecinos:
                if not G.has_edge(nodo, vecino):  # Asegurarse de que no exista ya la arista
                    G.add_edge(nodo, vecino)

        # Asignar color a los nodos según el rango
        node_colors = []
        for node in G.nodes:
            if 0 <= node <= 15:
                node_colors.append('lightblue')
            elif 16 <= node <= 23:
                node_colors.append('lightcoral')
            else:
                node_colors.append('lightgreen')

        # Dibujar el grafo con los colores asignados
        plt.figure(figsize=(10, 10))
        nx.draw(G, with_labels=True, node_color=node_colors, node_size=700, font_size=10, font_color='black', edge_color='gray')
        plt.show()

    def shortest_distances(self, source_id):
        # Inicializa las "distancias" de todos los routers a infinito
        distances = {router.id: float("inf") for router in self.routers}
        # Establece la "distancia" del nodo de origen a 0
        distances[source_id] = 0
        # Inicializa una cola de prioridad
        pqueue = [(0, source_id)]
        heapify(pqueue)
        # Inicializa el conjunto de nodos visitados
        visited = set()
        # Inicializa el diccionario de predecesores
        predecessors = {router.id: None for router in self.routers}
        # Itera mientras pqueue no este vacia
        while pqueue:
            current_dist, current_node = heappop(pqueue) # Obtiene el nodo con la menor distancia
            if current_node in visited:
                continue # Salta si el nodo ya fue visitado
            visited.add(current_node) # En caso de no haber sido visitado, se añade al conjunto de visitados
            # Recorre los vecinos del nodo actual
            for neighbor in self.routers[current_node].table:
                # Calcula la "distancia", que en este caso es el ping
                tent_dist = current_dist + neighbor.ping
                # Si la distancia provisional es menor que la registrada, se actualiza
                if tent_dist < distances[neighbor.id]:
                    distances[neighbor.id] = tent_dist
                    heappush(pqueue, (tent_dist, neighbor.id))
                    # Actualiza el predecesor
                    predecessors[neighbor.id] = current_node

        return distances, predecessors

    """def  shortest_path(self, source_id, destiny_id):
        # Obtiene los predecesores al calcular las distancias más cortas
        _, predecessors = self.shortest_distances(source_id)
        # Inicializa el camino resultante
        path = []
        current_node = destiny_id
        # Se va llenando la lista, en reversa, de cada uno de los nodos pertenecientes al camino más corto
        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]
        # Se da vuelta a la lista
        path.reverse()

        return path"""
    
    def shortest_path(self, source_id, destiny_id):
        _, predecessors = self.shortest_distances(source_id)
        path = []
        current_node = destiny_id
        while current_node is not None:
            path.append(current_node)
            current_node = predecessors[current_node]
        path.reverse()
        return path if path[0] == source_id else []


    def test_controller(self):
        # Nodo de origen y destino
        source_id = 0
        destiny_id = 31

        # Calcular distancias más cortas
        distances, _ = self.shortest_distances(source_id)
        print(f"Distancias desde el nodo {source_id}: {distances}")

        # Calcular la ruta más corta
        path = self.shortest_path(source_id, destiny_id)
        print(f"Camino más corto desde el nodo {source_id} hasta el nodo {destiny_id}: {path}")


#Este if era solo para probarlo desde acá, pero ya lo pueden borrar
if __name__ == "__main__":
    controller = Controller()
    controller.man()
    controller.test_controller()
    controller.graph()