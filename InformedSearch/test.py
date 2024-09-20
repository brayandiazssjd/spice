
#1 = City(10, 10, 10, "name", [""])
#c2 = c1
#c2.name = "0"

#print(c1.name)

from CityController import CityController
from Controller import Controller
from GUI import GUI

def test_upload(city_controller):
    if len(city_controller.cities) == 30:
        print("test_upload PASSED")
    else:
        print("test_upload FAILED")

def test_adjmatrix(city_controller):
    matrix = city_controller.adjmatrix()
    if len(matrix) > 0 and all(isinstance(row, list) and row is not None for row in matrix):
        print("test_adjmatrix PASSED")
    else:
        print("test_adjmatrix FAILED")
    
    # Añadido para depurar
    for i, row in enumerate(matrix):
        if not row:
            print(f"Fila {i} de la matriz de adyacencia está vacía.")
        else:
            print(f"Fila {i} contiene: {row}")


def test_cdistance(city_controller):
    city1 = city_controller.cities[0]
    city2 = city_controller.cities[1]
    distance = city_controller.cdistance(city1, city2)
    if distance > 0:
        print("test_cdistance PASSED")
    else:
        print("test_cdistance FAILED")

def test_enruteA(controller):
    try:
        print("ANTES DE ENROUTE")
        route = controller.enruteA(23, 2)
        if len(route) > 0:
            print("test_enruteA PASSED")
            print(route)
        else:
            print("test_enruteA FAILED: La ruta está vacía")

        return route
    except Exception as e:
        print(f"test_enruteA FAILED: Ocurrió una excepción - {e}")
        return None

def test_enruteAA(controller):
    try:
        route = controller.enruteAA(23, 2)
        if len(route) > 0:
            print("test_enruteAA PASSED")
            print(route)
        else:
            print("test_enruteAA FAILED: La ruta está vacía")

        return route
    except Exception as e:
        print(f"test_enruteAA FAILED: Ocurrió una excepción - {e}")
        return None

"""def get_cities(routeId):
    routeCities = []
    for city_id in routeId:
        if isinstance(city_id, list):  # Si city_id es una lista, algo salió mal
            print(f"Error: city_id contiene una lista: {city_id}")
        else:
            city = city_controller.cities[city_id]  # Suponemos que city_id es un entero
            routeCities.append(city.name)
    return routeCities"""

"""def get_cities(route):
    ids, dis = route  # Desempaquetamos la lista de ids y la distancia total
    routeCities = []
    
    for city_id in ids:  # Solo iteramos sobre los ids de las ciudades
        city = city_controller.cities[int(city_id)]  # Nos aseguramos que city_id sea un entero
        routeCities.append(city.name)
    
    print(f"Distancia total: {dis}")  # Si deseas mostrar la distancia total también
    return routeCities"""

def get_cities(route):
    if not route or not route[0]:
        print("No se encontró ninguna ruta.")
        return [], 0  # Devuelve una lista vacía y 0 distancia si no hay ruta válida

    ids, total_distance = route  # Desempaquetamos la lista de ids y la distancia total
    city_names = [city_controller.cities[int(city_id)].name for city_id in ids]  # Obtenemos los nombres de las ciudades
    return city_names, total_distance

def get_mst_cities(mst, city_controller):
    mst_cities = []
    for edge_list in mst:
        for edge in edge_list:  # Cada lista contiene múltiples objetos Edge
            end_city = city_controller.cities[edge.to]  # Usamos `edge.to` para obtener la ciudad de destino
            mst_cities.append(f"{end_city.name} (peso: {edge.cost})")  # Añadimos el nombre de la ciudad y el costo
    return mst_cities



# Ejecutar pruebas
routeA = []
routeAA = []
city_controller = CityController()
city_controller.upload()
controller = Controller(city_controller)

test_upload(city_controller)
test_adjmatrix(city_controller)
test_cdistance(city_controller)
test_enruteA(controller)
test_enruteAA(controller)
# Ejecutar pruebas
routeIdA = test_enruteA(controller)
routeA, total_distanceA = get_cities(routeIdA)

routeIdAA = test_enruteAA(controller)
routeAA, total_distanceAA = get_cities(routeIdAA)

mst, total_cost = controller.prims_mst()
mst_cities = get_mst_cities(mst, city_controller)

gui = GUI(controller, routeA, routeAA, mst_cities, total_distanceA, total_distanceAA, total_cost)
gui.draw_graph()