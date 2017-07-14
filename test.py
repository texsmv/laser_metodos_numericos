from vpython import *
import numpy as np

'''
Para nuestro problema:
Nuestro X = Programa Z
Nuestro Y = Programa X
Nuestro Z = Programa Y
'''
def to_vector(x):
    v = vector(x[0], x[1], x[2])    
    return v

def points_to_vector(X):
    points = []
    for e in X:
        points.append(to_vector(e))
    return points

def getplanoXY(v):
    return vec(v.x, v.y, 0)

def getplanoYZ(v):
    return vec(0, v.y, v.z)

def getplanoXZ(v):
    return vec(v.x, 0, v.z)

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
        self.L = L
        self.b2 = b2
        self.art3 =  sphere(pos=self.brazo2.pos + self.brazo2.axis, radius=0.25, texture=textures.metal)
        self.Ppos = [np.array([-1,0,0]), np.array([1,0,0])]
        #self.pointer_direction = self.brazo2.axis
        self.pointer = cylinder(pos=self.art3.pos, axis=self.brazo2.axis - self.art3.pos, radius=0.05)
        self.pointer.visible = False
    def RotarBrazo1(self, angulo):
        n = 10000
        dangulo = angulo/n
        for i in range(0, n):
            rate(500000)
            self.brazo1.rotate(angle=radians(dangulo), axis=getplanoXY(self.art1.pos), origin=self.art1.pos)
            self.art2.rotate(angle=radians(dangulo), axis=getplanoXY(self.art1.pos), origin=self.art1.pos)
            self.brazo2.rotate(angle=radians(dangulo), axis=getplanoXY(self.art1.pos), origin=self.art1.pos)
            self.art3.pos = self.brazo2.pos + self.brazo2.axis
            
            

    def RotarBrazo2(self, angulo):
        n = 10000
        dangulo = angulo/n
        for i in range(0, n):
            rate(500000)
            self.brazo2.rotate(angle=radians(dangulo), axis=getplanoXZ(self.art2.pos) , origin=self.art2.pos)
            self.art3.pos = self.brazo2.pos + self.brazo2.axis
            

    def dibujar_puntos(self):
        self.puntos = points(pos=[vector(-1,0,0), vector(1,0,0)], radius=3,color=color.red)

    
    def apuntar_punto(self):
        self.pointer.visible = True
        self.pointer.pos = self.art3.pos
        temp = -self.L / self.brazo2.axis.y
        self.pointer.axis= vector(self.brazo2.axis.x * temp - self.brazo2.axis.x, self.brazo2.axis.y * temp -self.brazo2.axis.y , self.brazo2.axis.z * temp - self.brazo2.axis.z)
        self.pointer.color = vector(1,0,0)
        
        
    def borrar_punto(self):
        self.pointer.visible = False
        
        
#Inicializacion del Robot
R = Robot(5, 2.5, 2)
R.dibujar_puntos()
scene.autoscale = False
scene.autocenter = False
#Mover brazos
while True:
    R.apuntar_punto()
    R.RotarBrazo1(45)
    R.RotarBrazo2(-45)
    R.borrar_punto()
    
    
    
