# Numpy [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

import matplotlib.pyplot as plt
import random

def comprension_listas_generadores():
    print('Práctica con compresión de listas | Generadores')

    # Generar una lista a partir de
    # multiplicar por "2" todos los valores
    # de "numeros"
    numeros = [1, -5, -6, 4]
    numeros_cmp = [2*x for x in numeros]
    print(numeros_cmp)
    # numeros_cmp= [2, -10, -12, 8]

    print('Generador de listas')
    # Generar una nueva lista utilizando los datos
    # del rango para generar nuevos

    # Método tradicional con bucle
    lista = []
    for x in range(10):
        valor = 2*x
        lista.append(valor)

    print(lista)

    # Método con comprension de listas
    lista_generada = [2*x for x in range(10)]
    
    # Gráfico
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(range(10), lista_generada)
    plt.show()

    # Generar una nueva lista, utilizar el rango para
    # iterar cierta cantidad de veces (definir el tamaño)
    # de la lista, y generar datos en cada iteración.

    # Método tradicional con bucle
    lista = []
    for x in range(5):
        valor = random.randint(1, 6)
        lista.append(valor)

    # Método con comprensión de listas
    lista = [random.randint(1, 6) for x in range(5)]
    print(lista)

    print('terminamos comprension_listas_generadores')


def comprension_listas_filtrado():
    print('Práctica con compresión de listas | Filtrado')

    print('Generadores con filtro')
    # Generar una lista que tome los números pares
    # y reemplace los números impares por "0"
    numeros = [1, 2, 4, 6, 8, 3, 5]

    # Método tradicional con bucle
    lista = []
    for x in numeros:
        if(x % 2) == 0:
            valor = x
        else:
            valor = 0
        lista.append(valor)
    # lista [0, 2, 4, 6, 8, 0, 0]

    # Método con comprensión de listas
    lista = [x if(x % 2) == 0 else 0 for x in numeros]
    # lista [0, 2, 4, 6, 8, 0, 0]
    print(lista)

    # Generar una lista que solo tome los números pares
    # y descarte los números impares
    numeros = [1, 2, 4, 6, 8, 3, 5]

    # Método tradicional con bucle
    lista = []
    for x in numeros:
        if(x % 2) == 0:
            lista.append(x)
    # lista [2, 4, 6, 8]

    # Método con comprensión de listas
    lista = [x for x in numeros if(x % 2) == 0]
    # lista [2, 4, 6, 8]
    print(lista)

    print('terminamos def comprension_listas_filtrado')


def comprension_dataset():
    print('El poder de la comprension en datasets!')

    dataset = [{'id': '123', 'name': 'Inove'},
               {'id': '', 'name': 'NaN'},
               {'ipo': 'sfa'},
               {'id': '456', 'name': 'Python'},
               {'id': '789', 'name': 'Programador'},
               ]

    print('Crear un dataset a partir de otro, sin filtrar o modificar datos')
    lista = [x for x in dataset]
    print(lista)

    print('Del dataset original quedarnos unicamente con la columna id')
    # Ojo! Se podría usar x['id'] pero en el dataset puede existir el caso
    # donde no exista una fila con la key "id" y por eso se utiliza "get"
    # Cuando se utiliza "x.get" se puede especificar como segundo parámetro
    # que deseamos que retorno en caso de no encontrar la key buscada.
    # En este caso se esta eligiendo devolver un string vacio '' en caso
    # de no encontrar la key "id"
    lista_reducida = [x.get('id', '') for x in dataset]
    print(lista_reducida)

    # En cada iteración se genera un diccionario con key=id, es una lista
    # de diccionarios
    lista_diccionario_reducida = [{'id': x.get('id', '')} for x in dataset]
    print(lista_diccionario_reducida)

    print('Del dataset original eliminar aquellas filas con "id" invalido')
    # Utilizamos "isdigit" para evaluar si el string tiene forma de numero,
    # en caso de ser un caracter o un string vacio "isdigit" retorna "False"
    lista_filtrada = [x for x in dataset if x.get('id', '').isdigit() is True]
    print(lista_filtrada)

    print('Del dataset original eliminar aquellas filas con "id" invalido')
    print('y quedarnos unicamente con la columna name')
    # Acá ponemos todo a prueba! solo se está dejando como salvedad
    # que si existe la key "id" debe existir la key "name"
    lista_filtrada_reducida = [{'name': x['name']} for x in dataset if x.get('id', '').isdigit() is True]
    print(lista_filtrada_reducida)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    comprension_listas_generadores()
    comprension_listas_filtrado()
    # -----------------------------
    comprension_dataset()

    print("terminamos")