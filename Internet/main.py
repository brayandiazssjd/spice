'''
Workflow
0. Crear el 'internet'
1. Digita el nombre del router al que te quieres conectar
2. Digita nombre de la red de destino
3. Recibir el texto por consola
4. Ejecutar el algoritmo e imprime:
	4.1 Ruta de cada Packet
	4.2 Mensajes perdidos
	4.3 Tiempo que se demoró en llegar todo el mensaje
'''
from Controller import Controller

con = Controller()
con.man()

print("Redes disponibles:")
for p in con.routers:
	print(p.name, "->", p.id)
print("Digita el id del origen:")
origin = int(input())
print("Digita el id del destino:")
destiny = int(input())
print("Digita el mensaje:")
msg = str(input())

con.simulate(origin, destiny, msg)