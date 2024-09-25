
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
            mst_edges = get_route_edges(route, city_controller)
            mst = None
            mst_cities = []
            mst_total_cost = 0

        
        elif choice == '2':
            start = int(input("Ingrese el nodo de inicio: "))
            goal = int(input("Ingrese el nodo de destino: "))
            route = controller.enruteAA(start, goal)
            route_names, total_distance = get_cities(route)
            mst_edges = get_route_edges(route, city_controller)
            mst = None
            mst_cities = []
            mst_total_cost = 0

        elif choice == '3':
            mst, total_cost = controller.prims_mst()
            route_names = []
            total_distance = 0
            route = ([], 0)
            route_names = get_mst_cities(mst, city_controller)
            mst_edges = get_mst_edges(mst, city_controller)
            mst_total_cost = total_cost
        
        elif choice == '4':
            mst, total_cost = controller.kruskal_mst()
            route_names = []
            total_distance = 0
            route = ([], 0)
            route_names = get_mst_cities(mst, city_controller)
            mst_edges = get_mst_edges(mst, city_controller)
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
            mst_edges = get_route_edges(route, city_controller)
            mst = None
            mst_cities = []
            mst_total_cost = 0
        
        elif choice == '7': 
            break

        else:
            print("Opción inválida. Por favor, intente de nuevo.")
            continue

        # Mostrar el resultado en la GUI
        gui = GUI(controller, mst_total_cost)
        gui.draw_graph(route_names, mst_edges)

def get_cities(route):
    if not route or not route[0]:
        print("No se encontró ninguna ruta.")
        return [], 0  # Devuelve una lista vacía y 0 distancia si no hay ruta válida

    ids, total_distance = route  # Desempaquetamos la lista de ids y la distancia total
    city_names = [ct.cities[int(city_id)].name for city_id in ids]  # Obtenemos los nombres de las ciudades
    return city_names, total_distance

def get_route_edges(route, city_controller):
    # El primer elemento de 'route' es la lista de IDs de ciudades
    route_ids = route[0]
    
    # Lista para almacenar las aristas (edges) de la ruta
    route_edges = []

    # Iterar sobre los IDs de las ciudades en la ruta para crear las aristas
    for i in range(len(route_ids) - 1):
        city1 = city_controller.cities[route_ids[i]].name  # Ciudad origen
        city2 = city_controller.cities[route_ids[i + 1]].name  # Ciudad destino
        route_edges.append((city1, city2))  # Añadir la arista origen-destino a la lista

    return route_edges

def get_mst_cities(mst, city_controller):
    mst_cities = set()  # Usamos un conjunto para evitar duplicados
    for u, edges in enumerate(mst):  # u representa el nodo origen
        start_city_name = city_controller.cities[u].name  # Ciudad origen
        mst_cities.add(start_city_name)  # Añadir ciudad origen al conjunto
        for edge in edges:
            end_city_name = city_controller.cities[edge.to].name  # Ciudad destino
            mst_cities.add(end_city_name)  # Añadir ciudad destino al conjunto
    return list(mst_cities)  # Convertir el conjunto de vuelta a una lista

def get_mst_edges(mst, city_controller):
    mst_edges = []  # Lista para almacenar las aristas del MST
    for u, edges in enumerate(mst):  # u representa el nodo origen
        for edge in edges:
            # Agregar solo aristas únicas, evitando duplicados
            if (edge.to, u) not in mst_edges and (u, edge.to) not in mst_edges:
                start_city_name = city_controller.cities[u].name  # Ciudad origen
                end_city_name = city_controller.cities[edge.to].name  # Ciudad destino
                mst_edges.append((start_city_name, end_city_name))  # Añadir la conexión origen-destino
    return mst_edges

if __name__ == "__main__":

    main_menu()