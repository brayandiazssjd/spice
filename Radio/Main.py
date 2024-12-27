from Node import Node
from Graph import Graph
from Gui import Gui

def menu() -> int:
    print("\t1. Minimizar\n\t2. Agregar\n\t0. Salir\n\t\t-> ")
    try:
        return int(input())
    except ValueError:
        return -1
    
def get_d(neigh_name) -> int:
    print(f"Ingrese la distancia con {neigh_name}")
    try:
        return int(input())
    except ValueError:
        return get_d(neigh_name)

def add(g: Graph):
    print("Ingrese el nombre: ")
    node = Node(g.nodes_number, input())
    for n in g.nodes:
        d = get_d(n.name)
        node.neighbors.append((n, d))
        n.neighbors.append((node, d))
    g.add(node)

def loop() -> None:
    choice = menu()
    graph = Graph()
    graph.upload()
    gui = Gui(graph)

    while choice != 0:
        if choice == 1:
            gui.draw_graph()
        elif choice == 2:
            add(graph)
        else:
            print(f"La opcion {choice} no esta disponible")
        choice = menu()

    print("Bye Bye Bye...")

if __name__ == "__main__":
    print("Gimme Gimme Gimme...")
    loop()
