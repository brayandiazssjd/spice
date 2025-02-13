import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx


class Window:
    def __init__(self, mediator):
        self.color_nodes = []
        self.mediator = mediator
        self.root = tk.Tk()
        self.root.title("Grafo 3D con menú y selección de nodos")
        self.root.geometry("900x600")
        graph_data, self.node_dict = self.mediator.get_graph_data()  # Desempacar la tupla
        self.figura_grafo, self.G, self.pos = self.crear_grafo_3d_desde_rooms(graph_data) # Pasar graph_data
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing) # Detener programa al cerrar la ventana

        # Frame para el menú
        menu_frame = tk.Frame(self.root, width=250, bg="black")
        menu_frame.pack(side="left", fill="y")

        # Notebook para las pestañas
        self.notebook = ttk.Notebook(menu_frame)
        self.notebook.pack(fill="both", expand=True)

        # ----- Pestaña 1: Selección de Nodos -----
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Seleccionar Nodo")

        # Label
        self.menu_label = tk.Label(self.tab1, text="Seleccione un Nodo:", font=("Arial", 12))
        self.menu_label.pack(pady=5)

        # Usar los nodos generados en el grafo
        self.nodos_lista = list(self.G.nodes())  # Obtener los nodos del grafo automáticamente

        # Lista desplegable con buscador
        self.combobox_nodos = ttk.Combobox(self.tab1, values=self.nodos_lista, state="readonly")
        self.combobox_nodos.pack(pady=5)
        self.combobox_nodos.bind("<<ComboboxSelected>>", self.nodo_seleccionado)

        # Etiqueta para mostrar nodo seleccionado
        self.label_seleccion = tk.Label(self.tab1, text="Seleccionado: Ninguno", font=("Arial", 10))
        self.label_seleccion.pack(pady=5)

        # Lista de actividades
        self.actividades = [
            {"id": 0, "name": "Educación física", "external_noise": 40, "local_noise": 50, "start": 8, "end": 10},
            {"id": 1, "name": "Baile", "external_noise": 50, "local_noise": 60, "start": 8, "end": 10},
            {"id": 2, "name": "Yoga", "external_noise": 30, "local_noise": 20, "start": 8, "end": 10},
            {"id": 3, "name": "Cátedra", "external_noise": 20, "local_noise": 30, "start": 8, "end": 10},
            {"id": 4, "name": "Conferencia", "external_noise": 25, "local_noise": 35, "start": 8, "end": 10},
            {"id": 5, "name": "Debate", "external_noise": 35, "local_noise": 55, "start": 8, "end": 10},
            {"id": 6, "name": "Laboratorio", "external_noise": 15, "local_noise": 25, "start": 8, "end": 10},
            {"id": 7, "name": "Investigación", "external_noise": 20, "local_noise": 20, "start": 8, "end": 10},
            {"id": 8, "name": "Teatro", "external_noise": 35, "local_noise": 45, "start": 8, "end": 10}
        ]
        self.actividades_dict = {act["name"]: act["id"] for act in self.actividades}

        # Combobox para seleccionar una actividad
        self.combobox_actividades = ttk.Combobox(self.tab1, values=list(self.actividades_dict.keys()), state="readonly")
        self.combobox_actividades.pack(pady=5)
        self.combobox_actividades.bind("<<ComboboxSelected>>", self.actividad_seleccionada)

        # Etiqueta para mostrar la actividad seleccionada
        self.label_actividad = tk.Label(self.tab1, text="Actividad: Ninguna", font=("Arial", 10))
        self.label_actividad.pack(pady=5)

        # Botones con opciones
        ttk.Button(self.tab1, text="Info", command=self.info).pack(pady=5)
        ttk.Button(self.tab1, text="Cambiar actividad", command=self.cambiarAct).pack(pady=5)
        ttk.Button(self.tab1, text="Diagnosticar nodo", command=self.diagnosticar).pack(pady=5)
        ttk.Button(self.tab1, text="Optimizar", command=self.optimizar).pack(pady=5)
        
        # Frame para el grafo 3D
        self.graph_frame = tk.Frame(self.root)
        self.graph_frame.pack(side="right", fill="both", expand=True)

        # Mostrar la figura en la interfaz
        self.canvas = FigureCanvasTkAgg(self.figura_grafo, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        self.actualizar_colores_grafo()

        # Ejecutar la aplicación
        self.root.mainloop()

    def crear_grafo_3d_desde_rooms(self, graph_data): # Recibir graph_data
        G = nx.Graph()
        pos = {}

        for node_id, room in graph_data['nodes'].items(): # Acceder al diccionario directamente
            G.add_node(node_id)
            piso = node_id // 4
            habitacion = node_id % 4
            x = habitacion // 2
            y = habitacion % 2
            z = piso
            pos[node_id] = (x, y, z)

        for node_id, edges in graph_data['edges'].items(): # Acceder al diccionario directamente
            for neighbor_id, weight in edges:
                G.add_edge(node_id, neighbor_id)

        fig = plt.figure(figsize=(6, 6))
        ax = fig.add_subplot(111, projection='3d')

        self.G = G  # Asignar el grafo a self.G

        for node_id, (x, y, z) in pos.items():
            ax.scatter(x, y, z, c='blue', s=100)
            ax.text(x, y, z, str(node_id), color='black', fontsize=14, fontweight='bold')

        for edge in G.edges():
            x, y, z = zip(*[pos[n] for n in edge])
            ax.plot(x, y, z, c='black')

        ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
        return fig, G, pos
    
    def actualizar_colores_grafo(self):
        self.colores = ["lightgreen", "yellow", "red", "blue"]
        ax = self.figura_grafo.gca()

        for node_id, (x, y, z) in self.pos.items():
            node = self.node_dict[node_id]
            self.color_nodes.append(node)
            print("SELF.NODE_DICT OOOOOOU YEAAAAH")
            print(node.color)
            if node and node.color is not None:
                color_index = node.color
                if 0 <= color_index < len(self.colores):
                    color = self.colores[color_index]
                elif color_index == -1:
                    color = 'gray'

            for scatter in ax.collections:
                try:  # Manejar la excepción si _offsets3d no está disponible
                    x_scatter, y_scatter, z_scatter = scatter._offsets3d  # Acceder a las coordenadas 3D
                    # x_scatter, y_scatter y z_scatter son arrays 1D
                    for i in range(len(x_scatter)): # Iterar sobre las coordenadas de cada punto del scatter
                        if abs(x_scatter[i] - x) < 1e-6 and abs(y_scatter[i] - y) < 1e-6 and abs(z_scatter[i] - z) < 1e-6:
                            scatter.set_facecolors(color)
                            break
                    else:
                        continue
                    break
                except AttributeError:  # _offsets3d no está disponible (scatter 2D)
                    continue  # Saltar al siguiente scatter plot

        self.canvas.draw()

    def nodo_seleccionado(self, event):
        seleccionado = self.combobox_nodos.get()
        self.label_seleccion.config(text=f"Seleccionado: {seleccionado}")

    def actividad_seleccionada(self, event):
        nombre_actividad = self.combobox_actividades.get()
        actividad_id = self.actividades_dict[nombre_actividad]
        self.label_actividad.config(text=f"Actividad: {nombre_actividad} (ID: {actividad_id})")

    def info(self):
        id = self.combobox_nodos.get()
        if id:
            try:
                id = int(id)
                act = self.mediator.getInfo(id)
                messagebox.showinfo("Información del Nodo", f"Actividad: {act}")
            except (ValueError, KeyError):
                messagebox.showerror("Error", "ID de nodo inválido o no encontrado.")
        else:
            messagebox.showwarning("Advertencia", "Debe seleccionar un nodo para ver la información.")

    def cambiarAct(self):
        nombre_actividad = self.combobox_actividades.get()
        if nombre_actividad:
            nodo_id = self.combobox_nodos.get()
            act_select = next((act for act in self.actividades if act["name"] == nombre_actividad), None)
            if self.mediator:
                self.mediator.cambiarAct(act_select, nodo_id)
        self.actualizar_colores_grafo()

    def diagnosticar(self):
        nodo_id = self.combobox_nodos.get()
        if nodo_id:  # Asegurarse de que se ha seleccionado un nodo
            try:
                nodo_id = int(nodo_id)  # Convertir a entero si es necesario
                node = self.node_dict[nodo_id]  # Obtener el objeto Node del diccionario
                color = node.color  # Obtener el color del nodo

                # Llamar a la función diagnosticar del mediator, pasando el color
                if self.mediator:
                    message = self.mediator.diagnosticar(nodo_id, color)  # Pasar nodo_id y color
                    messagebox.showinfo("Diagnóstico", message)

            except (ValueError, KeyError):
                messagebox.showerror("Error", "ID de nodo inválido o no encontrado.")
        else:
            messagebox.showwarning("Advertencia", "Debe seleccionar un nodo para diagnosticar.")

    def optimizar(self):
        self.mediator.optimizar(self.color_nodes)

        _, self.node_dict = self.mediator.get_graph_data()

        self.redibujar()
        amarillos = []
        for node in self.color_nodes:
            if node.color == 1:
                amarillos.append(node)
        if amarillos:
            self.mediator.optimizar_restantes(amarillos)
            self.redibujar()

        messagebox.showinfo("Optimización", "¡Optimización del edificio completa!")

    def redibujar(self):
        # ***ACTUALIZAR LA FIGURA EXISTENTE***
        ax = self.figura_grafo.gca()  # Obtener el axes 3D existente
        ax.clear()  # Limpiar el axes

        # Volver a dibujar los elementos del grafo en el axes limpio
        for node_id, (x, y, z) in self.pos.items():
            ax.scatter(x, y, z, c='blue', s=100)
            ax.text(x, y, z, str(node_id), color='black', fontsize=14, fontweight='bold')

        for edge in self.G.edges():
            x, y, z = zip(*[self.pos[n] for n in edge])
            ax.plot(x, y, z, c='black')

        ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])

        self.canvas.draw()  # Redibujar el canvas

        self.actualizar_colores_grafo()

    def on_closing(self):
        if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
            self.root.destroy()
            sys.exit()
