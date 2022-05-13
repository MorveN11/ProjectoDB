import random


def generateRandomNums(nro_digitos, nro_numeros):
    numero_minimo = 1
    numero_maximo = 10
    lista_numeros = []
    for i in range(1, nro_digitos):
        numero_minimo *= 10
        numero_maximo *= 10
    numero_maximo -= 1
    index = 0
    while index < nro_numeros:
        numero_aleatorio = str(random.randint(numero_minimo, numero_maximo))
        if numero_aleatorio not in lista_numeros:
            lista_numeros.append(numero_aleatorio)
            index += 1
    return lista_numeros


def generateCI():
    numero_minimo = 1
    numero_maximo = 10
    for i in range(1, 7):
        numero_minimo *= 10
        numero_maximo *= 10
    numero_maximo -= 1
    numero_aleatorio = str(random.randint(numero_minimo, numero_maximo))
    return numero_aleatorio


def generateCSE():
    numero_minimo = 1
    numero_maximo = 10
    for i in range(1, 3):
        numero_minimo *= 10
        numero_maximo *= 10
    numero_maximo -= 1
    numero_aleatorio = str(random.randint(numero_minimo, numero_maximo))
    return numero_aleatorio


def generateRandomNit():
    numero_minimo = 1
    numero_maximo = 10
    for i in range(1, 8):
        numero_minimo *= 10
        numero_maximo *= 10
    numero_maximo -= 1
    numero_aleatorio = str(random.randint(numero_minimo, numero_maximo))
    return numero_aleatorio


def generateNumViv():
    numero_minimo = 1
    numero_maximo = 10
    for i in range(1, 2):
        numero_minimo *= 10
        numero_maximo *= 10
    numero_maximo -= 1
    numeroViv = chr(random.randint(65, 90)) + "-" + str(random.randint(numero_minimo, numero_maximo))
    return numeroViv


def generateNumCell():
    numero_minimo = 6
    numero_maximo = 8
    for i in range(1, 8):
        numero_minimo *= 10
        numero_maximo *= 10
    numero_maximo -= 1
    cell = "+591 " + str(random.randint(numero_minimo, numero_maximo))
    return cell
