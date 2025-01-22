from RadioStation import RadioStation


class RadioStationFactory:

    def create_list(self, names):
        return [RadioStation(i, names[i]) for i in range (len(names))]

    def create_all_attrs(self, color: str, neighbors, id: int, name: str) -> RadioStation:
        node = RadioStation(id, name)
        node.neighbors = neighbors
        node.color = color
        return node
    
    def clone(self, nodes) -> list:
        return [self.create_all_attrs(node.color, [], node.id, node.name) for node in nodes]

    def link(self, distances, nodes):
        for i in range(len(nodes)):
            nodes[i].neighbors = distances[i]
        return nodes
