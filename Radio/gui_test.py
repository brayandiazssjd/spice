from Gui import Gui
from Graph import Graph

g = Graph()
g.upload()

gui = Gui(g)
gui.draw_graph()
