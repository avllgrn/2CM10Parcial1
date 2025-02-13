from os import system
from random import randrange

def unaFuncionConRandrange():
    V = []
    print(V, type(V))

    n = int(input('Cuantos datos? '))

    for i in range(n):
        V.append(randrange(60,81))

    for i in range(len(V)):
        print(i, V[i], type(V[i]))

    print(V, type(V), len(V))

    posicion = int(input('Cual posicion? '))
    V[posicion] = -123
    print(V, type(V), len(V))

if __name__ == '__main__':
    system('cls')

    unaFuncionConRandrange()
    print()