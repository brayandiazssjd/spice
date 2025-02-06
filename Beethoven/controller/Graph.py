from model.Node import Node

class Graph:
    def __init__(self, rooms):
        self.nodes = {} 

        # Crear nodos usando los objetos Room originales
        for room in rooms:
            self.nodes[room.id] = Node(room.id, room)  # Aquí guardas el Room en el Node

        # Conectar nodos (accediendo a room.room.relations)
        for node in self.nodes.values():  # node es un Node, que contiene un Room en node.room
            room = node.room  # Recuperamos el objeto Room
            if room is not None and room.relations:  # Verificamos que tiene relaciones
                for neighbor_room, wall in room.relations:
                    if neighbor_room.id in self.nodes:
                        node.add_edge(neighbor_room.id, wall)


