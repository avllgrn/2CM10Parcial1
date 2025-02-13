from os import system

def unaFuncionConListaDeEnteros():
    lista = [12, 3, -54, 6, 8]
    print(lista, type(lista), len(lista))

    for i in range(len(lista)):
        print(i, lista[i], type(lista[i]))

def unaFuncionConListaDeFlotantes():
    lista = [1.2, 3., -5.4, 6.0]
    print(lista, type(lista), len(lista))

    for i in range(len(lista)):
        print(i, lista[i], type(lista[i]))

def unaFuncionConListaDeStrings():
    lista = ['casa', 'puerta', 'ventana']
    print(lista, type(lista), len(lista))

    for i in range(len(lista)):
        print(i, lista[i], type(lista[i]))

if __name__ == '__main__':
    system('cls')
    unaFuncionConListaDeEnteros()
    print()
    unaFuncionConListaDeFlotantes()
    print()
    unaFuncionConListaDeStrings()
    print()
