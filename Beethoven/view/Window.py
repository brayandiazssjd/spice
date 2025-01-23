import tkinter as tk
from tkinter import ttk
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx

# Función para crear el grafo 3D
def crear_grafo_3d():
    # Crear un grafo
    G = nx.Graph()
    pisos = 5
    habitaciones_por_piso = 4

    # Generar nodos y posiciones en 3D
    pos = {}
    for piso in range(pisos):
        z = piso  # Coordenada Z representa el piso
        for i, (x, y) in enumerate([(0, 0), (0, 1), (1, 1), (1, 0)]):
            nodo = piso * habitaciones_por_piso + i
            pos[nodo] = (x, y, z)
            G.add_node(nodo)
            if i > 0:
                G.add_edge(nodo, nodo - 1)
        G.add_edge(piso * habitaciones_por_piso, piso * habitaciones_por_piso + habitaciones_por_piso - 1)

    for piso in range(pisos - 1):
        for i in range(habitaciones_por_piso):
            G.add_edge(piso * habitaciones_por_piso + i, (piso + 1) * habitaciones_por_piso + i)

    # Dibujar el grafo
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Dibujar nodos
    for node, (x, y, z) in pos.items():
        ax.scatter(x, y, z, c='blue', s=100)
        ax.text(x, y, z, str(node), color='black', fontsize=8)

    # Dibujar aristas
    for edge in G.edges():
        x = [pos[edge[0]][0], pos[edge[1]][0]]
        y = [pos[edge[0]][1], pos[edge[1]][1]]
        z = [pos[edge[0]][2], pos[edge[1]][2]]
        ax.plot(x, y, z, c='black')

    # Configurar ejes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    return fig

# Configuración de la ventana principal
root = tk.Tk()
root.title("Grafo 3D con menú")
root.geometry("900x600")

# Frame para el menú
menu_frame = tk.Frame(root, width=200, bg="lightgray")
menu_frame.pack(side="left", fill="y")

# Opciones en el menú
menu_label = tk.Label(menu_frame, text="Menú", font=("Arial", 16), bg="lightgray")
menu_label.pack(pady=10)

boton1 = ttk.Button(menu_frame, text="Opción 1")
boton1.pack(pady=5)

boton2 = ttk.Button(menu_frame, text="Opción 2")
boton2.pack(pady=5)

boton3 = ttk.Button(menu_frame, text="Opción 3")
boton3.pack(pady=5)

# Frame para el grafo 3D
graph_frame = tk.Frame(root)
graph_frame.pack(side="right", fill="both", expand=True)

# Crear y mostrar el grafo 3D
figura_grafo = crear_grafo_3d()
canvas = FigureCanvasTkAgg(figura_grafo, master=graph_frame)
canvas.get_tk_widget().pack(fill="both", expand=True)

# Ejecutar la aplicación
root.mainloop()