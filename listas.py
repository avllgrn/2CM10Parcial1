from os import system
from random import randrange

def generaRand(tam, ini, fin):
    l = []

    for i in range(tam):
        l.append(randrange(ini, fin))

    return l

def muestraLista(l):

    tam = len(l)
    for i in range(tam):
        print(f'[{i}] = {l[i]}')

def concatenaListas(l1, l2):
    l3 = []

    for dato in l1:
        l3.append(dato)

    for dato in l2:
        l3.append(dato)

    return l3

def acumulaVectores(l1, l2):
    s = 0

    for dato in l1:
        #print(s, dato)
        s += dato

    for dato in l2:
        #print(s, dato)
        s += dato

    return s

def sumaVectores(V1, V2):

    V3 = []

    if len(V1) == len(V2):
        for i in range(n):
            V3.append(V1[i]+V2[i])

    return V3

def restaVectores(V1, V2):

    V3 = []

    if len(V1) == len(V2):
        for i in range(n):
            V3.append(V1[i]-V2[i])

    return V3

def promediaVectores(n,P1,P2,P3):

    Prom = []

    for i in range(n):
        Prom.append((P1[i]+P2[i]+P3[i])/3)


    return Prom

def muestraCalificaciones(n,P1,P2,P3,Promedio):

    print('Alumno',end='\t')
    for j in range(3):
        print(f'P{j+1}',end='\t')
    print('Promedio\n')
    
    for i in range(n):
        print(f'{i+1}\t{P1[i]}\t{P2[i]}\t{P3[i]}\t{Promedio[i]}')

if __name__ == '__main__':
    system('cls')
    n = int(input('Dame n '))

    P1 = generaRand(n,0,11)
    P2 = generaRand(n,0,11)
    P3 = generaRand(n,0,11)

    Promedio = promediaVectores(n,P1,P2,P3)

    muestraCalificaciones(n,P1,P2,P3,Promedio)
    