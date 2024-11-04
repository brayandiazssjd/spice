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
                if i != j:
                    distances[i].append((nodes[j], matrix[i, j]))

        nf.link(distances, nodes) 
        self.nodes = nodes

        

