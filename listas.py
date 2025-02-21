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

if __name__ == '__main__':
    system('cls')
    n = int(input('Dame n '))
    m = int(input('Dame m '))

    A = generaRand(n,0,11)
    B = generaRand(m,0,11)

    s = acumulaVectores(A,B)

    print('\nA')
    muestraLista(A)
    print('\nB')
    muestraLista(B)
    print(f'\ns = {s}')
    