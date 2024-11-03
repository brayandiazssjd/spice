from Node import Node


class NodeFactory:
	"""docstring for NodeFactory"""

	def create_list(self, names):
		return [Node(i, names[i]) for i in range (len(names))]

	def link(self, distances, nodes):
		for i in range(len(nodes)):
			nodes[i].neights = distances[i]
		return nodes
	
