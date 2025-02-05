import tkinter as tk
from tkinter import ttk
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx
from controller import Mediator

class Window:

    def __init__(self, mediator: Mediator):
        self.mediator = mediator

    # Función para crear el grafo 3D
    def crear_grafo_3d():
        global pos, G  # Guardamos las posiciones y el grafo para su uso posterior

        G = nx.Graph()
        pisos = 5
        habitaciones_por_piso = 4
        pos = {}

        # Generar nodos y posiciones en 3D
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
            ax.text(x, y, z, str(node), color='black', fontsize=14, fontweight='bold')

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
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])

        return fig

    # Función para manejar la selección de un nodo
    def nodo_seleccionado(event):
        seleccionado = combobox_nodos.get()
        label_seleccion.config(text=f"Seleccionado: {seleccionado}")

    # Crear ventana principal
    root = tk.Tk()
    root.title("Grafo 3D con menú y selección de nodos")
    root.geometry("900x600")

    # Frame para el menú
    menu_frame = tk.Frame(root, width=250, bg="lightgray")
    menu_frame.pack(side="left", fill="y")

    # Notebook para las pestañas
    notebook = ttk.Notebook(menu_frame)
    notebook.pack(fill="both", expand=True)

    # ----- Pestaña 1: Selección de Nodos -----
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text="Seleccionar Nodo")

    # Label
    menu_label = tk.Label(tab1, text="Seleccione un Nodo:", font=("Arial", 12))
    menu_label.pack(pady=5)

    # Crear y mostrar el grafo 3D
    figura_grafo = crear_grafo_3d()

    # Usar los nodos generados en el grafo
    nodos_lista = list(G.nodes())  # Obtener los nodos del grafo automáticamente

    # Lista desplegable con buscador
    combobox_nodos = ttk.Combobox(tab1, values=nodos_lista, state="readonly")
    combobox_nodos.pack(pady=5)
    combobox_nodos.bind("<<ComboboxSelected>>", nodo_seleccionado)

    # Etiqueta para mostrar nodo seleccionado
    label_seleccion = tk.Label(tab1, text="Seleccionado: Ninguno", font=("Arial", 10))
    label_seleccion.pack(pady=5)

    #Funciones de los botones
    def editar():
        pass
    def cambiarAct():
        pass

    def diagnosticar():
        pass

    # Botones con opciones
    boton1 = ttk.Button(tab1, text="Editar", command=editar)
    boton1.pack(pady=5)

    boton2 = ttk.Button(tab1, text="Cambiar actividad", command=cambiarAct)
    boton2.pack(pady=5)

    boton3 = ttk.Button(tab1, text="Diagnosticar", command=diagnosticar)
    boton3.pack(pady=5)

    # ----- Pestaña 2: Prueba -----
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text="Solución")

    # Botón de prueba
    boton_prueba = ttk.Button(tab2, text="Ejecutar solución")
    boton_prueba.pack(pady=20)

    # Frame para el grafo 3D
    graph_frame = tk.Frame(root)
    graph_frame.pack(side="right", fill="both", expand=True)

    # Mostrar la figura en la interfaz
    canvas = FigureCanvasTkAgg(figura_grafo, master=graph_frame)
    canvas.get_tk_widget().pack(fill="both", expand=True)

    # Ejecutar la aplicación
    root.mainloop()