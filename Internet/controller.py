from router import Router

class Controller:
    def __init__(self):
        self.routers = []  

    def man(self):
        ip = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

        x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310]
        y = [310, 300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
        vel = [100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 102, 204, 306, 408, 150, 250, 350, 450, 820, 840, 860, 880, 900, 920, 940, 960]
        
        #pylint: disable= too-many-function-args
        self.routers = [Router(ip[i], x[i], y[i], vel[i]) for i in range(0, 31)]

        #Vecinos 
        r = self.routers

        neighs=[
            [r[1],r[15], r[17]], #0
            [r[0], r[17], r[2]], #1
            [r[1],r[3],r[17]], #2
            [r[2], r[18], r[17]], #3
            [r[18]], #4
            [r[19],r[18]], #5
            [r[7]], #6
            [r[8],r[6],r[20]], #7
            [r[7], r[20]], #8
            [r[22],r[21]], #9
            [r[21]], #10
            [r[22],r[21]], #11
            [r[22]], #12
            [r[23]], #13
            [r[15],r[16]], #14
            [r[0], r[14],r[23],r[16]], #15
            [r[14],r[15],r[17],r[23]], #16
            [r[0],r[1],r[2],r[3],r[16],r[22]], #17
            [r[3], r[4], r[5], r[19],r[21],r[23]], #18
            [r[20], r[5],r[18]], #19
            [r[21],r[8], r[7],r[19]], #20
            [r[11],r[10],r[9],r[20],r[18]], #21
            [r[12],r[11],r[9],r[17]], #22
            [r[15], r[13],r[16],r[18]], #23
            [r[31],r[25],r[26],r[30]], #24
            [r[24],r[26],r[27],r[29]], #25
            [r[25], r[27],r[24]], #26
            [r[28],r[26],r[25],r[31]], #27
            [r[29],r[30],r[27]], #28
            [r[28],r[25]], #29
            [r[28],r[31],r[24]], #30
            [r[30],r[24], r[27]] #31 
        ]

        for i in range(0, 31):
            r[i].table = neighs[i]
        

#Hacer conexiones, digamos hay una lista de rputers, modificar el atributo tabl,e, que es la tabla donde el router tiene 
#las conexiones, coge el primer router, el atributo table, a table lo conecta con el puntero de la ip del segundo router y así

#Entonces:
#1. Enumerar routers
#2. Ver cómo se hizo en municipios y ponerlo así acá
#3. Tratar de imprimir el grafo en consola
#