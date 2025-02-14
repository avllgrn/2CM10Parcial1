from os import system

if __name__ == '__main__':
    system('cls')

    n = int(input('Dame n '))

    s = 0
    for i in range(n+1):
        s = s+i
        print(f'i = {i}\ts = {s}')
    print(f'\ns = {s}\n')

    p = 1
    for i in range(1, n+1):
        p = p*i
        print(f'i = {i}\tp = {p}')
    print(f'\np = {p}')