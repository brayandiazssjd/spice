from City import City


c1 = City(10, 10, 10, "name", [""])
c2 = c1
c2.name = "0"

print(c1.name)