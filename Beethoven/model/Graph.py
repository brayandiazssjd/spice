from model.Node import Node


class Graph:
    def __init__(self, nodes):
        self.nodes = {}

        for node in nodes:
            self.nodes[node.id] = node

        # Conectar nodos (iterando directamente sobre node.edges)
        for node in self.nodes.values():
            for neighbor_id, weight in node.edges:  # Itera directamente sobre la lista
                if neighbor_id in self.nodes:
                    neighbor_node = self.nodes[neighbor_id]
                    # Si quieres un grafo no dirigido, añade la arista inversa:
                    # neighbor_node.add_edge(node.id, weight)
