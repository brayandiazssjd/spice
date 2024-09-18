
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

def get_cities(routeId):
    routeCities = []
    for city_id in routeId:
        if isinstance(city_id, list):  # Si city_id es una lista, algo salió mal
            print(f"Error: city_id contiene una lista: {city_id}")
        else:
            city = city_controller.cities[city_id]  # Suponemos que city_id es un entero
            routeCities.append(city.name)
    return routeCities


# Ejecutar pruebas
routeA = []
routeAA = []
city_controller = CityController()
city_controller.upload()
controller = Controller(city_controller.adjmatrix(), city_controller)

test_upload(city_controller)
test_adjmatrix(city_controller)
test_cdistance(city_controller)
test_enruteA(controller)
test_enruteAA(controller)
routeIdA = test_enruteA(controller)
print(f"routeId: {routeIdA}")
routeA = get_cities(routeIdA)
routeIdAA = test_enruteAA(controller)
routeAA = get_cities(routeIdAA)

gui = GUI(city_controller, routeA, routeAA)
gui.draw_graph()
