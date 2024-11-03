from Node import Node


class NodeFactory:
	"""docstring for NodeFactory"""
	def create(self, id: int, name: str) -> Node:
		node: Node = Node()
		node.id = id
		node.name = name
		return node

	def create_list(self, names):
		return [self.create(i, names[i]) for i in range (len(names))]

	def link(self, distances, nodes):
		for i in range(len(nodes)):
			nodes[i].neights = distances[i]
		return nodes
	
