from os import system
from random import randrange

if __name__ == '__main__':
    system('cls')
    V = []
    n = int(input('Dame n '))

    i=0
    while i<n:
        V.append(randrange(-100, 101))
        i += 1

    i=0
    while i<n:
        print(f'V[{i}] = {V[i]}')
        i += 1
    print()
    
    s = 0
    i=0
    while i<n:
        s = s + V[i]
        i += 1
        #print(f'V[{i}] = {V[i]}\ts = {s}')

    print(f'\ns = {s}')
    if n>0:
        promedio = s/n
        print(f'promedio = {promedio}')
        i += 1

    menor = V[0]
    posMenor = 0
    i=0
    while i<n:
       #print(f'menor = {menor}, = V[{posMenor}]')
       if V[i] < menor:
           menor = V[i]
           posMenor = i
       i += 1
    print(f'menor = {menor}, = V[{posMenor}]')


    mayor = V[0]
    posMayor = 0
    i=0
    while i<n:
       #print(f'mayor = {mayor}, = V[{posMayor}]')
       if V[i] > mayor:
           mayor = V[i]
           posMayor = i
       i += 1
    print(f'mayor = {mayor}, = V[{posMayor}]')

    menoresQuePromedio = 0
    i=0
    while i<n:
        if V[i] < promedio:
            menoresQuePromedio += 1
        i += 1
    print(f'Hay {menoresQuePromedio} menores que el promedio')


    mayorQuePromedio = 0
    i=0
    while i<n:
        if V[i] > promedio:
            mayorQuePromedio += 1
        i += 1
    print(f'Hay {mayorQuePromedio} mayores que el promedio')


    