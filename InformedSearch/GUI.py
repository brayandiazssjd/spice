from Controller import Controller

import networkx as nx
import matplotlib.pyplot as plt

class GUI:

    def __init__(self, controller, mst_total_cost=None):
        self.controller = controller
        """self.routeA = routeA
        self.routeAA = routeAA
        self.mst_cities = mst_cities
        self.total_distanceA = total_distanceA
        self.total_distanceAA = total_distanceAA
        self.choice = choice"""
        self.mst_total_cost = mst_total_cost
        self.g = nx.Graph()

    def create_graph(self):
        G = nx.Graph()

        adj_matrix = self.controller._Controller__matrix  # Acceder a la matriz de adyacencia

        for city_id, edges in enumerate(adj_matrix):
            city = self.controller._Controller__ct.cities[city_id]  # Obtener la ciudad por su ID
            G.add_node(city.name, pos=(city.lon, city.lat))  # Usar latitud y longitud para las posiciones

            for edge in edges:
                neighbor = self.controller._Controller__ct.cities[edge.to]  # Vecino conectado
                distance = edge.cost  # Usar el costo del `Edge` como la distancia
                G.add_edge(city.name, neighbor.name, weight=distance)  # Agregar la arista con el peso
        
        self.g = G  # Asigna el grafo creado a self.g para usarlo en draw_graph()

def draw_graph(self, route=None, mst_edges=None):
    # Declarar el tamaño de la ventana
    plt.figure(figsize=(19, 9))

    # Crear el grafo y asignar posiciones
    self.create_graph()
    pos = nx.get_node_attributes(self.g, 'pos')  # Obtener las posiciones para dibujar

    # Crear una lista para asignar colores a los nodos
    if route:
        node_colors = ['green' if node in route else 'blue' for node in self.g.nodes()]
    else:
        node_colors = 'blue'

    # Dibujar el grafo completo con nodos y aristas
    nx.draw(self.g, pos, with_labels=True, node_size=300, node_color=node_colors, font_size=7)

    # Dibujar las aristas (conexiones) con los pesos (distancias)
    edge_labels = nx.get_edge_attributes(self.g, 'weight')
    edge_labels = {k: f'{v:.2f}' for k, v in edge_labels.items()}
    nx.draw_networkx_edge_labels(self.g, pos, edge_labels=edge_labels, font_size=7, label_pos=0.3)

    # Resaltar las aristas del MST en rojo si existe un MST
    if mst_edges:
        for edge in mst_edges:
            city1, city2 = edge
            if city1 in pos and city2 in pos:  # Verifica que las ciudades estén en el grafo
                nx.draw_networkx_edges(self.g, pos, edgelist=[(city1, city2)], edge_color='red', width=2)

    # Mostrar información sobre el costo total del MST
    mst_text = f"Costo total: {self.mst_total_cost}"
    plt.text(0.49, 0.05, mst_text, ha='center', va='center', fontsize=7, transform=plt.gca().transAxes)

    # Mostrar el grafo
    plt.show(block=True)



    def draw_path(self, route, title="Resultado del Algoritmo"):
            plt.figure(figsize=(19, 9))
            self.create_graph()
            pos = nx.get_node_attributes(self.g, 'pos')  # Obtener las posiciones para dibujar

            # Dibujar solo el camino
            if route:
                route_edges = [(route[i], route[i + 1]) for i in range(len(route) - 1)]
                route_subgraph = self.g.edge_subgraph(route_edges)
                nx.draw(route_subgraph, pos, with_labels=True, node_size=300, node_color='red', font_size=7, edge_color='blue')

            plt.title(title)
            plt.show(block=True)

    """def __init__(self, city_controller, routeA, routeAA, mst_cities, total_distanceA, total_distanceAA, mst_total_cost):
            self.city_controller = city_controller
            self.routeA = routeA
            self.routeAA = routeAA
            self.mst_cities = mst_cities
            self.total_distanceA = total_distanceA
            self.total_distanceAA = total_distanceAA
            self.mst_total_cost = mst_total_cost
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
        # Declarar el tamaño de la ventana
        plt.figure(figsize=(19, 9))

        # Crear el grafo y asignar posiciones
        self.create_graph()
        pos = nx.get_node_attributes(self.g, 'pos')  # Obtener las posiciones para dibujar

        # Dibujar los nodos (ciudades)
        nx.draw(self.g, pos, with_labels=True, node_size=300, node_color='green', font_size=7)

        # Dibujar las aristas (conexiones) con los pesos (distancias)
        edge_labels = nx.get_edge_attributes(self.g, 'weight')

        # Redondear los valores de las distancias a 2 decimales
        edge_labels = {k: f'{v:.2f}' for k, v in edge_labels.items()}
        
        # Dibujar los pesos de las aristas con un tamaño de letra menor y una mejor posición
        nx.draw_networkx_edge_labels(self.g, pos, edge_labels=edge_labels, font_size=7, label_pos=0.3)

        # Mostrar información sobre las rutas y el MST
        plt.text(0.40, 0.15, f"Ruta A: {self.routeA} (Distancia total: {self.total_distanceA})", ha='center', va='center', fontsize=15, transform=plt.gca().transAxes)
        plt.text(0.40, 0.10, f"Ruta A*: {self.routeAA} (Distancia total: {self.total_distanceAA})", ha='center', va='center', fontsize=15, transform=plt.gca().transAxes)
        mst_text = f"PRIM MST: {', '.join(self.mst_cities)}\nCosto total: {self.mst_total_cost}"
        plt.text(0.49, 0.05, mst_text, ha='center', va='center', fontsize=7, transform=plt.gca().transAxes)
        # Mostrar el grafo
        plt.show(block=True)"""