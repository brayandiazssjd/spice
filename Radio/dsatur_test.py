from Graph import Graph

g = Graph()
g.upload()

result, colors_number = g.dsatur()
print(f"result: {result}, colors: {colors_number}")
print("Success")
