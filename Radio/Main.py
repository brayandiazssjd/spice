from configparser import Error


def menu() -> int:
	print("\t1. Minimizar\n\t2. Agregar\n\t\t-> ")
	try:
		return int(input())
	except Error:
		print("Opcion no valida")
		return 0

def draw() -> None:
	pass

def minimize() -> None:
	pass

def loop(choice: int) -> None:
	while(choice != 0):
		if choice == 1:
			minimize()
		elif choice == 2:
			draw()
		else:
			print(f"La opcion {choice} no esta disponible")
		choice = menu()

if __name__ == "__main__":
	print("I am... your father 🤖")
	loop(menu())