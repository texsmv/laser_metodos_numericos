from vpython import *    

'''
Para nuestro problema:
Nuestro X = Programa Z
Nuestro Y = Programa X
Nuestro Z = Programa Y
'''

#Obtener axis en el plano X
def getplanoX(v):
    return vec(v.x, 0, 0)

#Obtener axis en el plano Y
def getplanoY(v):
    return vec(0, v.y, 0)

#Obtener axis en el plano Z
def getplanoZ(v):
    return vec(0, 0, v.z)

#Dibujas ejes
origen = vec(0, 0, 0)

vecx = vec(5, 0, 0)
vecy = vec(0, 5, 0)
vecz = vec(0, 0, 5)

ejex = arrow(pos=vec(0, 0, 0), axis=vec(5, 0, 0), shaftwidth=0.1)
ejey = arrow(pos=vec(0, 0, 0), axis=vec(0, 5, 0), shaftwidth=0.1)
ejez = arrow(pos=vec(0, 0, 0), axis=vec(0, 0, 5), shaftwidth=0.1)

ejex.color = vec(1, 0, 0)
ejey.color = vec(0, 1, 0)
ejez.color = vec(0, 0, 1)

#Dibujar mesa
def DibujarMesa(largo, alto, ancho):
    return box(pos=vec(0, -alto/2, ancho/2), length=largo, height=alto, width=ancho, texture=textures.wood)
mesa = DibujarMesa(10, 0.2, 16)

#Luz
luz = local_light(pos=vec(-5, 5, 0), color=color.white)

#Declaracion del Robot
class Robot:
    def __init__(self, L, b1, b2):
        self.parante = cylinder(pos=vec(0, 0, 0), axis=vec(0, L, 0), radius=0.2, texture=textures.metal)
        self.brazo1 = cylinder(pos=vec(0, L, 0), axis=vec(0, 0, b1), radius=0.2, texture=textures.metal)
        self.brazo2 = cylinder(pos=vec(0, L, b1), axis=vec(0, -b2, 0), radius=0.2, texture=textures.metal)
        self.art1 = sphere(pos=vec(0, L, 0), radius=0.2, texture=textures.metal)
        self.art2 = sphere(pos=vec(0, L, b1), radius=0.2, texture=textures.metal)

    def RotarBrazo1(self, angulo):
        n = 100
        dangulo = angulo/n
        for i in range(0, n):
            rate(100)
            self.brazo1.rotate(angle=radians(dangulo), axis=getplanoY(self.art1.pos), origin=self.art1.pos)
            self.art2.rotate(angle=radians(dangulo), axis=getplanoY(self.art1.pos), origin=self.art1.pos)
            self.brazo2.rotate(angle=radians(dangulo), axis=getplanoY(self.art1.pos), origin=self.art1.pos)

    def RotarBrazo2(self, angulo):
        n = 100
        dangulo = angulo/n
        for i in range(0, n):
            rate(100)
            self.brazo2.rotate(angle=radians(dangulo), axis=getplanoZ(self.art2.pos), origin=self.art2.pos)

#Inicializacion del Robot
R = Robot(5, 2.5, 2)

#Mover brazos
while True:
    rate(5)
    R.RotarBrazo1(45)
    R.RotarBrazo2(-45)
