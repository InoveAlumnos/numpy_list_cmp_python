#!/usr/bin/env python
'''
Numpy [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"

import numpy as np
import time
import random


def metodos_numpy():
    print('Ejemplos de implementaciones con numpy')
    print('Método SUM')
    v1 = np.array([1, 5, -2, 10, 2])

    # Sumar todos los elementos de un array numpy
    suma_total = np.sum(v1)
    print('Suma total:', suma_total)

    # Calcular el promedio de todos los elementos de
    # un array numpy
    promedio = np.mean(v1)
    print('Promedio:', promedio)

    # Ordenar todos los elementos de un array numpy
    ordenados = np.sort(v1)
    print('Array ordenado', ordenados)


def numpy_where_diff():
    # Ejemplos de uso del método where y diff
    print('Método Where')

    # Crear un array numpy a partir de una lsita
    l1 = list(range(10))
    v1 = np.asanyarray(l1)

    # Crear un nuevo array que solo tengo los numeros
    # mayores a 3 del array numy y los demás reemplazar por cero
    # where(condicion, returno verdadero, retorno falso)
    where_v1 = np.where(v1 > 3, v1, 0)
    print(where_v1)

    # Crear un nuevo array que solo tengo los numeros
    # pares del array numy y los demás reemplazar por cero
    # where(condicion, returno verdadero, retorno falso)
    where_v1 = np.where((v1 % 2) == 0, v1, 0)
    print(where_v1)
    # [0 0 2 0 4 0 6 0 8]


def numpy_mask():
    # Ejemplos de uso de máscaras en numpy
    print('Numpy Mask')

    # Crear un array numpy
    v1 = np.array([1, 2, 4, 7])

    # Crear la máscara para solo quedarnos con
    # los números mayores a 1
    mask_one = v1 > 1
    v1_one = v1[mask_one]
    
    print(v1_one)

    # Crear la máscara para solo quedarnos con
    # los números pares
    mask_par = (v1 % 2) == 0
    v1_pares = v1[mask_par]
    
    print(v1_pares)
    # [2 4]


def expresion_map_lambda():
    print('Lambda expression y map')
    # Crear una funcion lambda que multiplique por 2
    # el valor pasado a la función

    mult_by_2 = lambda x: 2*x
    print(mult_by_2(3))  # resultado = 6

    # Utilizar "map" para aplicar una función
    # a toda una lista de forma iterativa
    # En este caso se utilizará la función
    # "abs()"
    numeros = [1, -5, -6, 4]
    numeros_abs = list(map(abs, numeros))
    print(numeros_abs)
    # [1, 5, 6, 4]

    # Ahora utilizar map para mapear nuestra función
    # lambda y aplicarla a toda la lista (iterar)
    numeros = [1, -5, -6, 4]
    numeros_mult_by_2 = list(map(mult_by_2, numeros))
    print(numeros_mult_by_2)
    # [2, -10, -12, 8]

    # El potencial de la lambda expression es poderla
    # definirla dentro del map (in line)
    numeros = [1, -5, -6, 4]
    numeros_lambda = list(map(lambda x: 2*x, numeros))
    print(numeros_lambda)
    # [2, -10, -12, 8]

    # SI lo tuviera que hacer con bucles:
    lista_pares_bucle = []
    for numero in numeros:
        valor = 2*numero
        lista_pares_bucle.append(valor)


def comprension_listas():
    print('Práctica con compresión de listas')

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

    print('Filtro')
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
    # En cada iteración se genera un diccionario con key=id, es una lista
    # de diccionarios
    lista_reducida = [{'id': x.get('id', '')} for x in dataset]
    print(lista_reducida)

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
    # ----------------------------
    metodos_numpy()
    numpy_where_diff()
    numpy_mask()
    # ----------------------------
    expresion_map_lambda()
    comprension_listas()
    # ----------------------------
    # Bonus Track - comprension listas + diccionarios
    comprension_dataset()
