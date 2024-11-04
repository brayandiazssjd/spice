from Node import Node
from Graph import Graph

def menu() -> int:
	print("\t1. Minimizar\n\t2. Agregar\n\t0. Salir\n\t\t-> ")
	try:
		return int(input())
	except ValueError:
		return -1

def draw() -> None:
	pass

def get_d(neigh_name) -> int:
    print(f"Ingrese la distancia con {neigh_name}")
    try:
        return int(input())
    except ValueError:
        return get_d(neigh_name)

def add(g: Graph):
    print("Ingrese el nombre: ")
    node = Node(g.count, input())
    for n in g.nodes:
        d = get_d(n.name)
        node.neights.append((n, d))
        n.neights.append((node, d))
    g.add(node)


def minimize() -> None:
	pass

def loop(choice: int) -> None:
	if choice == 0:
		return
	elif choice == 1:
		minimize()
	elif choice == 2:
		draw()
	else:
		print(f"La opcion {choice} no esta disponible")
	return loop(menu())

	

if __name__ == "__main__":
	print("I am... your father 🤖")
	loop(menu())
