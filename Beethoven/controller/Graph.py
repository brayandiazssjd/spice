
class Graph:

    def __init__(self, rooms):
        self.nodes = {}  # Diccionario para mapear id de la room a su nodo
        
        # Crear nodos
        for room in rooms:
            self.nodes[room.id] = Node(room.id, room)
        
        # Crear conexiones
        for room in rooms:
            node = self.nodes[room.id]
            for relation in room.relations:
                neighbor_room, wall = relation
                neighbor_node = self.nodes[neighbor_room.id]
                node.add_edge(neighbor_node, wall)
