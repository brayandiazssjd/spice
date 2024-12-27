from Node import Node


class NodeFactory:
    """docstring for NodeFactory"""

    def create_list(self, names):
        return [Node(i, names[i]) for i in range (len(names))]

    def create_all_attrs(self, color: str, neighbors, id: int, name: str) -> Node:
        node = Node(id, name)
        node.neighbors = neighbors
        node.color = color
        return node
    
    def clone(self, nodes) -> list:
        return [self.create_all_attrs(node.color, [], node.id, node.name) for node in nodes]

    def link(self, distances, nodes):
        for i in range(len(nodes)):
            nodes[i].neighbors = distances[i]
        return nodes
