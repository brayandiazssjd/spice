from Controller import Controller

import networkx as nx
import matplotlib.pyplot as plt

class GUI:

    def __init__(self, city_controller):
        self.city_controller = city_controller  # Recibe el controlador de ciudades
        self.g = nx.Graph()

    def create_graph(self):
        G = nx.Graph()
        
        for city in self.city_controller.cities:  # Accede a la lista de ciudades desde el controlador
            G.add_node(city.name, pos=(city.lon, city.lat))
            
            for neighbor in city.neighs:
                distance = self.city_controller.cdistance(city, neighbor)  # Usar el método cdistance desde el controlador
                G.add_edge(city.name, neighbor.name, weight=distance)
                
        self.g = G  # Asigna el grafo creado a self.g para usarlo en draw_graph()

    def draw_graph(self):
        # Crear el grafo y asignar posiciones
        self.create_graph()
        pos = nx.get_node_attributes(self.g, 'pos')  # Obtener las posiciones para dibujar

        # Dibujar los nodos (ciudades)
        nx.draw(self.g, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=8)

        # Dibujar las aristas (conexiones) con los pesos (distancias)
        edge_labels = nx.get_edge_attributes(self.g, 'weight')

        # Redondear los valores de las distancias a 2 decimales
        edge_labels = {k: f'{v:.2f}' for k, v in edge_labels.items()}
        
        # Dibujar los pesos de las aristas con un tamaño de letra menor y una mejor posición
        nx.draw_networkx_edge_labels(self.g, pos, edge_labels=edge_labels, font_size=7, label_pos=0.3)

        # Mostrar el grafo
        plt.show(block=True)
