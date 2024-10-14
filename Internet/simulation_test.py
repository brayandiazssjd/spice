from Controller import Controller


con = Controller()
con.man()

print("Redes disponibles:")
for p in con.routers:
	print(p.name, "->", p.id)
	p.controller = con
origin = 0
destiny = 31
msg = "asdfaosdmvaopeasfdafasdfsadfasdfasdfaifkmaoweif"

con.simulate(origin, destiny, msg)