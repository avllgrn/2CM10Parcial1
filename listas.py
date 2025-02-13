from os import system
from random import randrange

def unaFuncionConInput():
    V = []
    print(V, type(V))

    n = int(input('Cuantos datos? '))

    for i in range(n):
        V.append(float(input(f'Ingresa dato {i} ')))
        print(V, type(V), len(V))

    for i in range(len(V)):
        print(i, V[i], type(V[i]))

    print(V, type(V), len(V))

def unaFuncionConRandrange():
    V = []
    print(V, type(V))

    n = int(input('Cuantos datos? '))

    for i in range(n):
        V.append(randrange(60,81))
        print(V, type(V), len(V))

    for i in range(len(V)):
        print(i, V[i], type(V[i]))

    print(V, type(V), len(V))

if __name__ == '__main__':
    system('cls')
    
    unaFuncionConInput()
    print()
    unaFuncionConRandrange()
    print()