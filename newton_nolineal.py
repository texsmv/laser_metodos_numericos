from math import *

def mult_matriz(A,B):
    n = len(A)
    m = len(B[0])
    C = []
    for i in range(len(A)):
        C.append([0]*(len(B[0])))
    p = len(A[0])
    for i in range(n):
        for j in range(m):
            for k in range(p):
                C[i][j] += A[i][k]*B[k][j];
    return C

def suma_matriz(A,B):
    n = len(A)
    m = len(A[0])
    for i in range(n):
        for j in range(m):
            A[i][j] = A[i][j] + B[i][j]
    return A

def resta_matriz(A,B):
    n = len(A)
    m = len(A[0])
    for i in range(n):
        for j in range(m):
            A[i][j] = A[i][j] - B[i][j]
    return A

def convert_matriz2vector(A):
    a = []
    for i in range(len(A)):
        a.append(A[i][0])
    return a

def convert_vector2matriz(a):
    A = []
    for i in range(len(a)):
        A.append([a[i]])
    return A

#make vector null
def make_vector_null(n):
    return [0]*n

def sust_regre(A,b):
    n = len(A)
    X = make_vector_null(n)
    for i in range(n-1,-1,-1):
        s = 0
        for j in range(i+1,n):
            s += A[i][j]*X[j]
        X[i] = (b[i]-s)/A[i][i]
    return X

def sust_progre(A,b):
    n = len(A)
    X = make_vector_null(n)
    for i in range(n):
        s = 0
        for j in range(i):
            s += A[i][j]*X[j]
        X[i] = (b[i]-s)/A[i][i]
    return X

def suma_vector(a,b):
    c = a[:]
    if(len(a) == len(b)):
        for i in range(len(a)):
            c[i] += b[i]
        return c
    else:
        return

def resta_vector(a,b):
    c = a[:]
    if(len(a) == len(b)):
        for i in range(len(a)):
            c[i] -= b[i]
        return c
    else:
        return

def vector_x_escalar(a,e):
    c = a[:]
    for i in range(len(a)):
        c[i] *= e
    return c

#make matriz identidad
def make_matriz_identidad(n):
    M = []
    for i in range(n):
        aux = make_vector_null(n)
        for j in range(n):
            if(i==j):
                aux[i] = 1
        M.append(aux)
    return M

#make matriz null
def make_matriz_null(n):
    M = []
    aux = make_vector_null(n)
    for i in range(n):
        M.append(aux)
    return M

#swap function
def swap(A,i,j):
    aux = A[i]
    A[i] = A[j]
    A[j] = aux
    return A

def descomposicion_PLU(A):
    n = len(A)
    I = make_matriz_identidad(n)
    P = I
    L = make_matriz_null(n)
    U = A
    for  j in range(0,n-1):
        MaxPos = j
        Max = abs(U[MaxPos][j])
        for i in range(j,n):
            if(abs(U[i][j]) > Max):
                Max = abs(U[i][j])
                MaxPos = i
        if( MaxPos != j):
            swap(U,MaxPos,j)
            swap(P,MaxPos,j)
            swap(L,MaxPos,j)
        for r in range(j+1,n):
            m = -U[r][j]/(U[j][j] + 1)
            L[r][j] = -m
            for k in range(len(U[r])):
                U[r][k] += m*U[j][k]
    L = suma_matriz(L,I)
    PLU = []
    PLU.append(P)
    PLU.append(L)
    PLU.append(U)
    return PLU
    
def calc_descomposicion_PLU(A,b):
    PLU = descomposicion_PLU(A)
    Pb = convert_matriz2vector(mult_matriz(PLU[0],convert_vector2matriz(b)))
    Y = sust_progre(PLU[1],Pb)
    X = sust_regre(PLU[2],Y)
    return X

def F(X): #los puntos mas?
    F = []
    F.append(2.5*cos(X[0]) + 5*tan(X[1])*sin(X[0]) - (7))
    F.append(2.5*sin(X[0]) - 5*tan(X[1])*cos(X[0]) - (15))
    return F

def JacobAprox(X0,h):
    n = len(X0)
    I = make_matriz_identidad(n)
    JF = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            JF[i][j] = (F(suma_vector(X0,vector_x_escalar(I[j],h)))[i] - F(X0)[i])/h
    return JF

def restringir_angulos(X0, x, y):
    if X0[0]%6.28319 > pi:
        X0[0] -= 2*pi
    elif X0[0]%6.28319 < -pi:
        X0[0] += 2*pi
    if X0[1]%pi > pi/2:
        X0[1] -= pi
    elif X0[1]%pi < pi/2:
        X0[1] += pi
    if abs(X0[0])%6.28319 > pi/2:
        fi = X0[0] - atan(y/x)
        X0[0] -= 2*fi
        X0[1] = -X0[1]
    return X0

def newton_nolineal(X0,N):
    for i in range(N):
        
        JF = JacobAprox(X0,0.00000000000001)
        d = calc_descomposicion_PLU(JF,F(X0))
        X0 = resta_vector(X0,d)
    X0 = restringir_angulos(X0, 7, 15)
    return X0

'''def main():
    X0 = [-1.6,1.6]
    X = newton_nolineal(X0,100)'''
  

































    
