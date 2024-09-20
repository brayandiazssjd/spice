menu = "Opciones: \n\t1 para Kruskal's MST\n\t2 para Prim's MST\n\t3 para Djistra\n\t4 para Bellman Ford\n\t5 para A\n\t 6 para A*\n\t0 para salir"

print(menu)
option = int(input())
adj_matrix = []

while option != 0:
	if option == 1:
		# Generar mst por kruscal
		# Hacer el plot
		pass
	elif option == 2:
		# Generar mst por prim
		# Hacer el plot
		pass
	elif option == 3:
		#dibujar todo el grafo
		#colorear el resultado del djikstra
		pass
	elif option == 4:
		#dibujar todo el grafo
		#colorear el resultado del bellman
		pass
	elif option == 5:
		#dibujar todo el grafo
		#colorear el resultado del A
		pass
	elif option == 6:
		#dibujar todo el grafo
		#colorear el resultado del A*
		pass
	else:
		print("Opción no disponible, inténte otra")
