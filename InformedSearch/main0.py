
from CityController import CityController
from Controller import Controller

# Ruta preferente por lo mejor
ct = CityController()
c = Controller(ct)

# Ruta preferente por la distacia "lineal" más corta
# main.py
from CityController import CityController
from Controller import Controller
from GUI import GUI

def main_menu():
    city_controller = CityController()
    city_controller.upload()
    controller = Controller(city_controller)
    verificar = 0 #Para verificar si es el algoritmo de Dijkstra o A*

    while True:
        print("\n--- Menú ---")
        print("1. Ejecutar Greedy Best-First Search (A)")
        print("2. Ejecutar A* Search (AA)")
        print("3. Ejecutar Algoritmo de Prim (MST)")
        print("4. Ejecutar Algoritmo de Kruskal (MST)")
        print("5. Ejecutar Dijkstra")
        print("6. Ejecutar Bellman Ford")
        print("7. Salir")

        choice = input("Seleccione una opción (1-7): ")

        if choice == '1':
            start = int(input("Ingrese el nodo de inicio: "))
            goal = int(input("Ingrese el nodo de destino: "))
            route = controller.enruteA(start, goal)
            route_names, total_distance = get_cities(route)
            mst = None
            mst_cities = []
            mst_total_cost = 0
        
        elif choice == '2':
            start = int(input("Ingrese el nodo de inicio: "))
            goal = int(input("Ingrese el nodo de destino: "))
            route = controller.enruteAA(start, goal)
            route_names, total_distance = get_cities(route)
            mst = None
            mst_cities = []
            mst_total_cost = 0

        elif choice == '3':
            mst, total_cost = controller.prims_mst()
            route_names = []
            total_distance = 0
            route = ([], 0)
            route_names = get_mst_cities(mst, city_controller)
            """print("MST Adjacency Matrix:")
            for i, neighbors in enumerate(mst):
                for edge in neighbors:
                    print(f"From {i} to {edge.to} with cost {edge.cost}")"""
            mst_total_cost = total_cost
        
        elif choice == '4':
            mst, total_cost = controller.kruskal_mst()
            route_names = []
            total_distance = 0
            route = ([], 0)
            route_names = get_mst_cities(mst, city_controller)
            mst_total_cost = total_cost

        elif choice == '5': #Dijkstra  
            start = int(input("Ingrese el nodo de inicio: "))
            goal = int(input("Ingrese el nodo de destino: "))
            total_distance = 0
            route = controller.dijkstra(start, goal)
            route_names, total_distance = get_cities(route)
            mst = None
            mst_cities = []
            mst_total_cost = 0

        elif choice == '6': #Bellman Formd  
            start = int(input("Ingrese el nodo de inicio: "))
            goal = int(input("Ingrese el nodo de destino: "))
            total_distance = 0
            route = controller.bellman(start, goal)
            route_names, total_distance = get_cities(route)
            mst = None
            mst_cities = []
            mst_total_cost = 0
        
        elif choice == '7': 
            break

        else:
            print("Opción inválida. Por favor, intente de nuevo.")
            continue

        # Mostrar el resultado en la GUI
        #print("Nombres de nodos en el grafo:", self.g.nodes())
        #print_original_graph(city_controller.adjmatrix())
        #compare_graphs(city_controller.adjmatrix(), mst)
        gui = GUI(controller, mst_total_cost)
        gui.draw_graph(route_names)

def get_cities(route):
    if not route or not route[0]:
        print("No se encontró ninguna ruta.")
        return [], 0  # Devuelve una lista vacía y 0 distancia si no hay ruta válida

    ids, total_distance = route  # Desempaquetamos la lista de ids y la distancia total
    city_names = [ct.cities[int(city_id)].name for city_id in ids]  # Obtenemos los nombres de las ciudades
    return city_names, total_distance

def get_mst_cities(mst, city_controller):
    mst_cities = set()  # Usamos un conjunto para evitar duplicados
    for u, edges in enumerate(mst):  # u representa el nodo origen
        start_city_name = city_controller.cities[u].name  # Ciudad origen
        mst_cities.add(start_city_name)  # Añadir ciudad origen al conjunto
        for edge in edges:
            end_city_name = city_controller.cities[edge.to].name  # Ciudad destino
            mst_cities.add(end_city_name)  # Añadir ciudad destino al conjunto
    return list(mst_cities)  # Convertir el conjunto de vuelta a una lista

"""def compare_graphs(original_adj_matrix, mst_adj_matrix):
    for u, neighbors in enumerate(mst_adj_matrix):
        for edge in neighbors:
            if not any(edge.to == v.to and edge.cost == v.cost for v in original_adj_matrix[u]):
                print(f"Error: Edge from {u} to {edge.to} with cost {edge.cost} is not in the original graph.")


def print_original_graph(adjmatrix):
    for u, neighbors in enumerate(adjmatrix):
        for edge in neighbors:
            print(f"From {u} to {edge.to} with cost {edge.cost}")"""


if __name__ == "__main__":

    main_menu()