from configparser import Error


def menu() -> int:
	print("\t1. Minimizar\n\t2. Agregar\n\t0. Salir\n\t\t-> ")
	try:
		return int(input())
	except Error:
		return -1

def draw() -> None:
	pass

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