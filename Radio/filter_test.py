from Graph import Graph

g = Graph()
g.upload()
print((g.get(lambda x: x.name == "La W")).id)
for n in g.filter():
    print(f"r: {n.name} n: {[nbr[0].name for nbr in n.neighbors]}")


