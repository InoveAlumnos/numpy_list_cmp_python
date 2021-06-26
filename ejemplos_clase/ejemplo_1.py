# Numpy [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

import numpy as np


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

    print("terminamos metodos_numpy")


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

    print("terminamos numpy_where_diff")


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

    print("terminamos numpy_mask")


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    metodos_numpy()
    numpy_where_diff()
    numpy_mask()

    print("terminamos")