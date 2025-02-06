class Node:

    def __init__(self, id: int, room):
        self.id = id
        self.room = room
        self.edges = []  # Lista de conexiones con otros nodos

    def add_edge(self, neighbor, wall):
        self.edges.append((neighbor, wall))  # Conexión con habitación y la pared que los une
