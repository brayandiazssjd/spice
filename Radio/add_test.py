from Main import add
from Graph import Graph
from uploadTest import adapt

g = Graph()
g.upload()
print(adapt(g.nodes[0].neights))

add(g)

print(adapt(g.nodes[0].neights))

