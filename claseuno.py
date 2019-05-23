# EJERCICIO 1
b=0
numeros_enteros = list()
while b < 100000:
    numeros_enteros.append(b)
    b=b+1

print(numeros_enteros)

numeros_enteros_pares = list()
numeros_enteros_nones = list()

for x in numeros_enteros:
    if (x % 2) == 0:
        numeros_enteros_pares.append(x)
    else:
        numeros_enteros_nones.append(x)

diccionario = {
    "Pares": numeros_enteros_pares,
    "Impares": numeros_enteros_nones
}

print(diccionario)

# EJERCICIO 2

def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x,y):
    return x/y

print(sumar(1, 2))
print(restar(3, 2))
print(multiplicar(3, 3))
print(dividir(8, 2))

# EJERCICIO 3

valorTotal = 0
datos = []
dicName = dict()
dicCity = dict()
dicItem = dict()

with open(r'C:\Users\Administrador\Downloads\File1.csv', 'r') as archivo:
    registros = archivo.read().splitlines()
    registros.pop(0)
    for r in registros:
        registro = r.split('\t')
        datos.append([str(registro[1]), str(registro[6]), str(registro[7]), float(registro[8])])
        valorTotal = valorTotal + float(registro[8])
        if str(registro[1]) in dicName:
            dicName[str(registro[1])] = dicName.get(str(registro[1])) + float(registro[8])
        else:
            dicName[str(registro[1])] = float(registro[8])

        if str(registro[6]) in dicCity:
            dicCity[str(registro[6])] = dicCity.get(str(registro[6])) + float(registro[8])
        else:
            dicCity[str(registro[6])] = float(registro[8])

        if str(registro[7]) in dicItem:
            dicItem[str(registro[7])] = dicItem.get(str(registro[7])) + float(registro[8])
        else:
            dicItem[str(registro[7])] = float(registro[8])

    print("Promedios por columna Name")
    for name, promedio in dicName.items():
        print('Nombre {}, promedio {}'.format(name, promedio/valorTotal))

    print("Promedios por columna City")
    for nameCity, promedioCity in dicCity.items():
        print('Nombre {}, promedio {}'.format(nameCity, promedioCity / valorTotal))

    print("Promedios por columna Item")
    for nameItem, promedioItem in dicItem.items():
        print('Nombre {}, promedio {}'.format(nameItem, promedioItem / valorTotal))

