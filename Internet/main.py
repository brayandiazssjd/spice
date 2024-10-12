'''
Workflow
0. Crear el 'internet'
1. Digita el nombre del router al que te quieres conectar
2. Digita nombre de la red de destino
3. Recibir el texto por consola
4. Ejecutar el algoritmo e imprime:
	4.1 Ruta de cada Packet
	4.2 Mensajes perdidos
	4.3 Tiempo que se demoró en llegar todo el mensaje
'''

import random

# Generate random edges
edges = []
for node in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH"]:
    num_edges = random.randint(2, 6)
    connected_nodes = random.sample(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH"], num_edges)
    for connected_node in connected_nodes:
        if node != connected_node:
            edges.append(f"{node} -- {connected_node}")

# Add edges to the Graphviz script
for edge in edges:
    print(edge)