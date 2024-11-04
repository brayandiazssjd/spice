from Node import Node
from NodeFactory import NodeFactory
import numpy as np

class Graph:
    def __init__(self):
        self.nodes = []

    @property
    def count(self):
        return len(self.nodes)

    def add(self, n: Node):
        self.nodes.append(n)

    #def minimize(self):
    def upload(self):
        nf = NodeFactory()
        names = ["FM", "Blue Radio", "Tropicana", "Olimpica", "La W", "La Calle"]
        nodes = nf.create_list(names)

        matrix = np.array([[0, 85, 175, 200, 50, 100],
                           [0, 0, 125, 175, 100, 160],
                           [0, 0, 0, 100, 200, 250],
                           [0, 0, 0, 0, 210, 220],
                           [0, 0, 0, 0, 0, 100],
                           [0, 0, 0, 0, 0, 0]])
        matrix = matrix + matrix.T
        print(matrix)
        distances = [[] for i in range(6)]
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if i != j and matrix[i, j] <= 150:  # Only connect is the distance is >= 150 km
                    distances[i].append((nodes[j], matrix[i, j]))

        nf.link(distances, nodes) 
        self.nodes = nodes

    #DSatur algorithm for coloring graph.
    def dsatur(self):

        colors = {node: -1 for node in self.nodes}
        saturation = {node: 0 for node in self.nodes}
        degree = {node: len(node.neights) for node in self.nodes}

        current_node = max(degree, key=degree.get)
        colors[current_node] = 0
        
        for neighbor, _ in current_node.neights:
            if colors[neighbor] == -1:
                saturation[neighbor] += 1

        while -1 in colors.values():
            candidates = [node for node in self.nodes if colors[node] == -1]
            current_node = max(candidates, key=lambda n: (saturation[n], degree[n]))

            used_colors = {colors[neighbor] for neighbor, _ in current_node.neights if colors[neighbor] != -1}
            color = 0
            while color in used_colors:
                color += 1
            colors[current_node] = color

            for neighbor, _ in current_node.neights:
                if colors[neighbor] == -1:
                    saturation[neighbor] += 1

        num_colors = max(colors.values()) + 1  # Total colors used
        return colors, num_colors