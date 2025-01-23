from typing import Callable, Optional
from RadioStation import RadioStation
from RadioStationFactory import RadioStationFactory


class Graph:
    def __init__(self):
        self.radio_stations: list[RadioStation] = []

    # Returns the number of nodes
    @property
    def nodes_number(self) -> int:
        return len(self.radio_stations)

    def add(self, rs: RadioStation) -> None:
        self.radio_stations.append(rs)

    def filter(self) -> list[RadioStation]:
        rsf = RadioStationFactory()
        filtered = rsf.clone(self.radio_stations)
        for rs in filtered:
            rs.neighbors = {(filtered[nbr.id], distance) for nbr, distance in self.radio_stations[rs.id].neighbors if distance <= 150}
        return filtered

    def get(self, condition: Callable[[RadioStation], bool]) -> Optional[RadioStation]:        
        for node in self.radio_stations:
            if condition(node):
                return node
        return None
            
    def upload(self) -> None:
        nf = RadioStationFactory()
        names = ["FM", "Blue Radio", "Tropicana", "Olimpica", "La W", "La Calle", "Nacional"
                 "Radioactiva", "RCN", "Mega", "LOS40", "Caracol", "Radio Uno", "Radio Rock", "RTVC",
                 "Mix"]
        nodes = nf.create_list(names)
        matrix= [[  0,  85, 175, 220,  50, 100, 174, 263, 176, 179, 187, 122, 181, 234, 156, 177],
                [ 85,   0, 125, 175, 100, 160, 258, 130, 157, 221, 151, 249, 230,  74, 212, 104],
                [175, 125,   0, 100, 200, 250, 156, 163, 189, 210, 153, 185, 174, 147, 192, 160],
                [200, 175, 100,   0, 210, 220, 183, 170, 149, 136, 251, 140, 172, 241, 265, 177],
                [ 50, 100, 200, 210,   0, 100,  89, 147, 129, 156, 204, 167, 228, 216, 191, 244],
                [100, 160, 250, 220, 100,   0, 176, 188, 209, 114, 152, 105, 216,  66, 195, 235],
                [174, 258, 156, 183,  89, 176,   0, 175, 238, 230, 184, 219, 188, 175, 122, 220],
                [263, 130, 163, 170, 147, 188, 175,   0, 276, 171, 166, 169, 168, 169, 107, 116],
                [176, 157, 189, 149, 129, 209, 238, 276,   0, 154, 146, 242, 139, 110, 245, 245],
                [179, 221, 210, 136, 156, 114, 230, 171, 154,   0, 140, 232, 165, 141, 214,  98],
                [187, 151, 153, 251, 204, 152, 184, 166, 146, 140,   0,  92, 244, 229, 195, 219],
                [122, 249, 185, 140, 167, 105, 219, 169, 242, 232,  92,   0, 203, 112, 197, 127],
                [181, 230, 174, 172, 228, 216, 188, 168, 139, 165, 244, 203,   0,  88, 208, 224],
                [234,  74, 147, 241, 216,  66, 175, 169, 110, 141, 229, 112,  88,   0, 118, 170],
                [156, 212, 192, 265, 191, 195, 122, 107, 245, 214, 195, 197, 208, 118,   0, 172],
                [177, 104, 160, 177, 244, 235, 220, 116, 245,  98, 219, 127, 224, 170, 172,   0]]
        distances = [{(nodes[j], matrix[i][j]) for j in range(len(nodes)) if j != i} for i in range(len(nodes))]
        nf.link(distances, nodes) 
        self.radio_stations = nodes
    
    # DSatur algorithm for coloring graph.
    def dsatur(self):
        nodes = self.filter()

        colors = {node.id : -1 for node in nodes}
        saturation = {node: 0 for node in nodes}
        degree = {node: self.nodes_number for node in nodes}

        current_node = max(degree, key=degree.get)
        colors[current_node.id] = 0
        
        for neighbor, _ in current_node.neighbors:
            if colors[neighbor.id] == -1:
                saturation[neighbor] += 1

        while -1 in colors.values():
            candidates = [node for node in nodes if colors[node.id] == -1]
            current_node = max(candidates, key=lambda n: (saturation[n], degree[n]))

            used_colors = {colors[neighbor.id] for neighbor, _ in current_node.neighbors if colors[neighbor.id] != -1}
            color = 0
            while color in used_colors:
                color += 1
            colors[current_node.id] = color

            for neighbor, _ in current_node.neighbors:
                if colors[neighbor.id] == -1:
                    saturation[neighbor] += 1

        num_colors = max(colors.values()) + 1  # Total colors used
        return colors, num_colors
