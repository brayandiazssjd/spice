from Graph import Graph
import networkx as nx
import matplotlib.pyplot as plt

class Gui:

	def __init__(self, graph):
		self.graph = graph

	def create_networkx_graph(self):
		G = nx.Graph()

		for node in self.graph.nodes:
			G.add_node(node.name)

			for neighbor, distance in node.neighbors:
				if distance <= 150:
					G.add_edge(node.name, neighbor.name, weight=distance)
        
		return G

	def draw_graph(self):
		G = self.create_networkx_graph()
		colors, num_colors = self.graph.dsatur()

		pos = nx.spring_layout(G)  # Posicionamiento automático de nodos

        # Mapear los colores a partir de node.name
		node_colors = [colors[self.get_node_by_name(node)] for node in G.nodes]  # Usamos node.name como clave directamente

		plt.figure(figsize=(10, 6))
		nx.draw(G, pos, with_labels=True, node_size=500, node_color=node_colors, cmap=plt.cm.Set3)
		edge_labels = nx.get_edge_attributes(G, 'weight')
		nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

		plt.show()
    
	def get_node_by_name(self, name):
		for node in self.graph.nodes:
			if node.name == name:
				return node
		return None
