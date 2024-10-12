from router import Router

class Controller:
    def __init__(self):
        self.routers = []  

    def man(self):
        ip = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

        x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310]
        y = [310, 300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
        vel = [100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 102, 204, 306, 408, 150, 250, 350, 450, 820, 840, 860, 880, 900, 920, 940, 960]
        
        self.routers = [Router(ip[i], x[i], y[i], vel[i], []) for i in range(0, 31)]
        


        
class Router(Sortable, Weightable):
    def __init__(self, ip, x, y, vel, table):
        self.ip = ip
        self.x = x
        self.y = y
        self.vel = vel
        self.table = table 

    def getId(self):
        return self.ip

    def weight(self, id):
        pass

    def send(self, route, data: Packet):
        pass

    def bsearch(self, ip):
        pass
#Hacer conexiones, digamos hay una lista de rputers, modificar el atributo tabl,e, que es la tabla donde el router tiene 
#las conexiones, coge el primer router, el atributo table, a table lo conecta con el puntero de la ip del segundo router y así

#Entonces:
#1. Enumerar routers
#2. Ver cómo se hizo en municipios y ponerlo así acá
#3. Tratar de imprimir el grafo en consola
#