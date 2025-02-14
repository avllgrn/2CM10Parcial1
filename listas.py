from os import system
from random import randrange

if __name__ == '__main__':
    system('cls')
    V = []
    n = int(input('Dame n '))

    for i in range(n):
        V.append(randrange(-100, 101))

    for i in range(n):
        print(f'V[{i}] = {V[i]}')
    print()
    
    s = 0
    for i in range(n):
        s = s + V[i]
        #print(f'V[{i}] = {V[i]}\ts = {s}')

    print(f'\ns = {s}')
    if n>0:
        promedio = s/n
        print(f'promedio = {promedio}')

    menor = V[0]
    posMenor = 0
    for i in range(n):
       #print(f'menor = {menor}, = V[{posMenor}]')
       if V[i] < menor:
           menor = V[i]
           posMenor = i
    print(f'menor = {menor}, = V[{posMenor}]')


    mayor = V[0]
    posMayor = 0
    for i in range(n):
       #print(f'mayor = {mayor}, = V[{posMayor}]')
       if V[i] > mayor:
           mayor = V[i]
           posMayor = i
    print(f'mayor = {mayor}, = V[{posMayor}]')

    menoresQuePromedio = 0
    for i in range(n):
        if V[i] < promedio:
            menoresQuePromedio += 1
    print(f'Hay {menoresQuePromedio} menores que el promedio')


    mayorQuePromedio = 0
    for i in range(n):
        if V[i] > promedio:
            mayorQuePromedio += 1
    print(f'Hay {mayorQuePromedio} mayores que el promedio')


    