#!/usr/bin/env python
'''
Numpy [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import numpy as np
import time
import random

top = 5000000


def metodos_numpy_vs_list():
    print('Ejemplos de implementaciones con numpy vs list')
    print('Método SUM')
    v1 = np.arange(top)
    l1 = list(range(top))

    time1 = time.time()
    np.sum(v1)
    time2 = time.time()
    numpy_time_ms = (time2-time1)*1000
    print('Numpy time: {:.2f}ms'.format(numpy_time_ms))

    time1 = time.time()
    sum(l1)
    time2 = time.time()
    list_time_ms = (time2-time1)*1000
    print('List time: {:.2f}ms'.format(list_time_ms))
    print('SUM: Numpy vs List x{:.2f}'.format(list_time_ms/numpy_time_ms))

    print('Método mean')
    v1 = np.arange(top)
    l1 = list(range(top))

    time1 = time.time()
    np.mean(v1)
    time2 = time.time()
    numpy_time_ms = (time2-time1)*1000
    print('Numpy time: {:.2f}ms'.format(numpy_time_ms))

    time1 = time.time()
    sum(l1) / len(l1)
    time2 = time.time()
    list_time_ms = (time2-time1)*1000
    print('List time: {:.2f}ms'.format(list_time_ms))
    print('MEAN: Numpy vs List x{:.2f}'.format(list_time_ms/numpy_time_ms))

    print('Método sort')
    v1 = np.arange(top)
    l1 = list(range(top))

    time1 = time.time()
    np.sort(v1)
    time2 = time.time()
    numpy_time_ms = (time2-time1)*1000
    print('Numpy time: {:.2f}ms'.format(numpy_time_ms))

    time1 = time.time()
    l1.sort()
    time2 = time.time()
    list_time_ms = (time2-time1)*1000
    print('List time: {:.2f}ms'.format(list_time_ms))
    print('SORT: Numpy vs List x{:.2f}'.format(list_time_ms/numpy_time_ms))


def numpy_where_diff():
    # Ejemplos de uso del método where y diff
    print('Método Where')

    l1 = list(range(top))
    v1 = np.asanyarray(l1)

    where_v1 = np.where((v1 % 2) == 0, v1, 0)
    # [0 0 2 0 4 0 6 0 8]

    time1 = time.time()
    np.where((v1 % 2) == 0, v1, 0)
    time2 = time.time()
    numpy_time_ms = (time2-time1)*1000
    print('Numpy time: {:.2f}ms'.format(numpy_time_ms))

    time1 = time.time()
    [x if (x % 2) == 0 else 0 for x in l1]
    time2 = time.time()
    list_time_ms = (time2-time1)*1000
    print('List time: {:.2f}ms'.format(list_time_ms))
    print('WHERE: Numpy vs List x{:.2f}'.format(list_time_ms/numpy_time_ms))

    print('Método Diff')
    v1 = np.array([1, 2, 4, 7])
    v1_diff = np.diff(v1)
    # [2-1, 4-2, 7-4]
    # [1 2 3]
    print(v1_diff)

    m = np.array([
                 [1, 5],
                 [3, 1],
                 [5, 10]
                 ])

    m_diff_por_fila = np.diff(m)
    # [[ 4]
    #  [-2]
    #  [ 5]]
    print(m_diff_por_fila)

    m_diff_por_columna = np.diff(m, axis=0)
    # [[ 2 -4]
    #  [ 2  9]]
    print(m_diff_por_columna)


def comprension_listas_vs_bucle():
    print('Comprension de listas vs bucles')
    # Deseamos crear una lista de números pares
    # que contenga todos los números del 0 al 1000000 inclusive
    rango = range(500001)

    time1 = time.time()
    # ----------------------------
    # Método tradicional con bucle
    lista_pares_bucle = []
    for i in rango:
        valor = 2*i
        lista_pares_bucle.append(valor)
    # ----------------------------
    time2 = time.time()
    bucle_time_ms = (time2-time1)*1000
    print('Bucle time: {:.2f}ms'.format(bucle_time_ms))

    time1 = time.time()
    # ----------------------------
    # Método con comprensión
    lista_pares_comp = [2*x for x in rango]
    # ----------------------------
    time2 = time.time()
    list_time_ms = (time2-time1)*1000
    print('Comprension time: {:.2f}ms'.format(list_time_ms))
    print('Comprension vs Bucle x{:.2f}'.format(bucle_time_ms/list_time_ms))


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # ----------------------------
    # Uso de Numpy vs bucles vs listas
    # queda para que el alumno chusmee
    metodos_numpy_vs_list()
    numpy_where_diff()
    # ----------------------------
    # Uso de comprension de listas vs bucles
    comprension_listas_vs_bucle()
