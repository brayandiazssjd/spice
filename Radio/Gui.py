from Graph import Graph
import networkx as nx
import matplotlib.pyplot as plt

class Gui:

    def __init__(self, graph: Graph):
        self.graph = graph

    def create_networkx_graph(self):
        G = nx.Graph()

        for node in self.graph.radio_stations:
            G.add_node(node.name)

            for neighbor, distance in node.neighbors:
                if distance <= 150:
                    G.add_edge(node.name, neighbor.name, weight=distance)
        
        return G

    def draw_graph(self):
        G = self.create_networkx_graph()
        colors, num_colors = self.graph.dsatur()
        print(f"Minimum number of colors: {num_colors}")
        pos = nx.spring_layout(G)  # Posicionamiento automático de nodos

        # Mapear los colores a partir de node.name
        node_colors = [colors[self.graph.get(lambda x : x.name == node).id] for node in G.nodes]  # Usamos node.name como clave directamente

        plt.figure(figsize=(10, 6))
        nx.draw(G, pos, with_labels=True, node_size=500, node_color=node_colors, cmap=plt.cm.Set3)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.show()
