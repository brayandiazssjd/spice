from typing import Optional
from Node import Node
from NodeFactory import NodeFactory


class Graph:
    def __init__(self):
        self.nodes = []

    # Returns the number of nodes
    @property
    def nodes_number(self):
        return len(self.nodes)

    def add(self, n: Node):
        self.nodes.append(n)

    def filter(self) -> list:
        nf = NodeFactory()
        filtered = nf.clone(self.nodes)
        for node in filtered:
            node.neighbors = [(filtered[pointer.id], distance) for pointer, distance in self.nodes[node.id].neighbors if distance <= 150]
        return filtered

    def get(self, condition) -> Optional[Node]:        
        for node in self.nodes:
            if condition(node):
                return node
        return None
            
    def upload(self):
        nf = NodeFactory()
        names = ["FM", "Blue Radio", "Tropicana", "Olimpica", "La W", "La Calle"]
        nodes = nf.create_list(names)
        matrix= [[0, 85, 175, 200, 50, 100],
                [85, 0, 125, 175, 100, 160],
                [175, 125, 0, 100, 200, 250],
                [220, 175, 100, 0, 210, 220],
                [50, 100, 200, 210, 0, 100],
                [100, 160, 250, 220, 100, 0]]
        distances = [[(nodes[j], matrix[i][j]) for j in range(len(nodes)) if j != i] for i in range(len(nodes))]
        nf.link(distances, nodes) 
        self.nodes = nodes
    
    # DSatur algorithm for coloring graph.
    def dsatur(self):
        nodes = self.filter()

        colors = {node: -1 for node in nodes}
        saturation = {node: 0 for node in nodes}
        degree = {node: self.nodes_number for node in nodes}

        current_node = max(degree, key=degree.get)
        colors[current_node] = 0
        
        for neighbor, _ in current_node.neighbors:
            if colors[neighbor] == -1:
                saturation[neighbor] += 1

        while -1 in colors.values():
            candidates = [node for node in nodes if colors[node] == -1]
            current_node = max(candidates, key=lambda n: (saturation[n], degree[n]))

            used_colors = {colors[neighbor] for neighbor, _ in current_node.neighbors if colors[neighbor] != -1}
            color = 0
            while color in used_colors:
                color += 1
            colors[current_node] = color

            for neighbor, _ in current_node.neighbors:
                if colors[neighbor] == -1:
                    saturation[neighbor] += 1

        num_colors = max(colors.values()) + 1  # Total colors used
        return colors, num_colors
