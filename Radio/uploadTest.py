from Graph import Graph

g = Graph()
g.upload()

def adapt(neights):
    return [(n[0].id, n[1]) for n in neights]

for n in g.nodes:
    print(f"node: {n.id}, neights: {adapt(n.neights)}")
