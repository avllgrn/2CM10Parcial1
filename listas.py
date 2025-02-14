from os import system
from random import randrange

if __name__ == '__main__':
    system('cls')

    n = int(input('Dame n '))

    s = 0
    for i in range(n+1):
        dato = randrange(1,5)
        s = s+dato
        print(f'dato = {dato}\ts = {s}')
    print(f'\ns = {s}\n')

    p = 1
    for i in range(1, n+1):
        dato = randrange(1,5)
        p = p*dato
        print(f'dato = {dato}\tp = {p}')
    print(f'\np = {p}')