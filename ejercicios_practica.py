#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import numpy as np


def ej1():
    print('Comenzamos a ponernos serios!')

    '''
    '''


def ej2():
    print('Comenzamos a ponernos serios!')

    '''
    '''


def ej3():
    print("Un poco de Numpy!")
    # Ejercicio de funciones
    # Se desea calcular los valores de salida de
    # una función senoidal, dado "X" como el conjunto
    # de valores que deben someter a la función "sin"
    
    # Conjunto de valores "X" en una lista
    x = list(np.arange(0,2*np.pi,0.1))

    # Utilizar compresión de listas para obtener la lista    
    # "y_list" que tenga todos los valores obtenidos como resultado
    # de someter cada valor de "X" a la función math.sin

    # y_list =

    # Conjunto de valores "X" en un arrany
    x = np.arange(0,2*np.pi,0.1)

    # Utilizar compresión de listas para obtener la lista    
    # "y_list" que tenga todos los valores obtenidos como resultado
    # de someter cada valor de "X" a la función np.sin
    
    # y_nump =


def ej4():
    print("Acercamiento a el uso de datos relacionales")
    # Transformar variable numéricas en categoricas
    # Se dispone del siguiente diccionario que traduce el número ID
    # de un producto en su nombre, por ejemplo:
    # NOTA: Esta información bien podría ser una tabla SQL: id | producto
    producto = {
                556070: 'Auto',
                704060: 'Moto',
                42135: 'Celular',
                1264: 'Bicicleta',
                905045: 'Computadora',
                }

    lista_compra_id = [556070, 905045, 42135, 5674, 704060, 1264, 42135, 3654]

    # Crear una nueva lista "lista_compra_productos" que transforme la lista
    # de realizada por "ID" de producto en lista por "nombre" producto
    # Iterar sobre la lista "lista_compra_id" para generar la nueva
    # NOTA: Tener en cuenta que puede haber códigos (IDs) que
    # no esten registrados.
    # en el sistema, en esos casos se debe almacenar en la lista
    # la palabra 'NaN', para ello puede hacer uso de condicionales 
    # PERO recomendamos leer atentamente el método "get" de diccionarios
    # que tiene un parametro configurable respecto a que sucede
    # sino encuentra la "key" en el diccionario.


def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    '''


if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
