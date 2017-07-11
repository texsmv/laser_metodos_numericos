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

#Dibujar robot
brazo1 = cylinder(pos=vec(0, 0, 0), axis=vec(0, 5, 0), radius=0.2, texture=textures.metal)
brazo2 = cylinder(pos=vec(0, 5, 0), axis=vec(0, 0, 2.5), radius=0.2, texture=textures.metal)
brazo3 = cylinder(pos=vec(0, 5, 2.5), axis=vec(0, -2, 0), radius=0.2, texture=textures.metal)

art1 = sphere(pos=vec(0, 5, 0), radius=0.2, texture=textures.metal)
art2 = sphere(pos=vec(0, 5, 2.5), radius=0.2, texture=textures.metal)

#Mover Brazo1
def RotarBrazo1(angulo):
    brazo2.rotate(angle=radians(angulo), axis=getplanoY(art1.pos), origin=art1.pos)
    art2.rotate(angle=radians(angulo), axis=getplanoY(art1.pos), origin=art1.pos)
    brazo3.rotate(angle=radians(angulo), axis=getplanoY(art1.pos), origin=art1.pos)

#Mover Brazo2
def RotarBrazo2(angulo):
    brazo3.rotate(angle=radians(angulo), axis=getplanoZ(art2.pos), origin=art2.pos)

#Mover brazos
while True:
    rate(5)
    RotarBrazo1(45)
    RotarBrazo2(-45)
