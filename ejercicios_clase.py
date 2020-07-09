#!/usr/bin/env python
'''
Numpy [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

import numpy as np
import math


def ej1():
    # Lambda expression
    # 1)
    # Realizar una funcion lambda que eleve al cuadrado
    # el número pasado como parámetro

    # potencia_2 = lambda x:......
    # pot_3 = potencia_2(3)

    # 2)
    # Utilice la función map para mapear una lambda expression
    # que retorne la potencia de 2 de cada numero en la lista numeros
    # El resultado (la potencia de cada numero) se debe ir almacenando
    # en una nueva lista
    # Nota: realizar la lambda expression "in line", es decir,
    # no declarar la lambda fuera del map sino diretamente dentro
    # Copiar la lambda creada en el paso anterior dentro del map

    # List de string
    numeros = [1, -5, 4, 3]

    # numeros_potencia = list(map....)


def ej2():
    # Lambda expression
    # 1)
    # Realizar una funcion lambda que retorne el tamaño
    # (len) de un string pasado como parámetro

    # len_string = lambda......

    # 2)
    # List de string
    palabras = ['Inove', 'casa', 'programacion']

    # Utilice la función map para mapear una lambda expression
    # que retorne el tamaño (len) de cada texto em cata iteración
    # de la lista de textos
    # El resultado (el len de cada palabra) se debe ir almacenando
    # en una nueva lista
    # Nota: realizar la lambda expression "in line"
    # Copiar la lambda creada en el paso anterior dentro del map

    # palabras_len = list(map....)


def ej3():
    # Práctica de comprensión de listas
    # 1)
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá tener un tamaño de 11
    # números, conteniendo del 0 al 10 inclusive

    # lista_0_10 = [......]

    # 2)
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá contener la tabla del 5,
    # desde el múltiplo 0 al múltiplo 10
    # El resultado esperado es:
    # [0 5 10 15 20 25 30 35 40 45 50]
    # Utilizar comprensión de listas para generar essa lista

    # tabla_5 = [......]

    # 3)
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá contener 10 números aleatorios,
    # estos números deberán estar entre el rango 1 al 30 representando
    # números posibles de un mes (los números pueden repetirse)

    # dias_mes = [.....]

    pass


def ej4():
    # Utilizar comprensión de listas con condicionales

    # 1)
    # Utilizar comprensión de listas para convertir
    # una lista de números como str en números tipo int
    # sería un conversor string --> int
    # Ojo! Tener cuidado con lo string/caracteres
    # que no son números, utilizar condicionales para detectarlos
    # reemplazar dicho str "no numérico" por 0
    list_numeros_str = ['5', '-2', '3', '', '7', 'NaN']

    # lista_numeros_int = [.....]


def ej5():
    # Utilizar comprensión de listas para filtrar

    accesos = [10, 50, 7, 5, 15, 25, 3, 4, 13]

    # La lista accesso contiene los números de ID de personal
    # que ingresaron por ese molinete

    # 1)
    # Generar una lista por comprensión de la lista "accesos"
    # una lista que solo contenga (filtrado) los ID de personal
    # entre 1 al 10 inclusive, se desea separar del grupo de accesos
    # los ID entre el 1 y 10.
    # De la lista resultante informar cuantas personas/personal
    # comprendido en dicho rango pasó por ese molinete

    # personal_1_10 = [.....]

    # 2)
    # Generar una lista por comprensión de la listas "accesos"
    # cuyo ID de personal esté dentro de los ID válidos para ingresar
    # por ese molinete:
    id_validos = [3, 4, 7, 8, 15]
    # Debe generar una nueva lista basada en "accesos" filtrada por los ID
    # aprobados en "id_validos".
    # TIP: Utilizar el operador "in" para chequear si un ID de accesos está
    # dentro de "id_validos"

    # personal_valido = [.....]
    pass


def ej6():
    # Ejercicio de funciones Numpy
    # Arme un array con el método np.arange
    # el cual este acotado entre 0 y 1000
    # De dicho array calcular las siguientes operaciones:

    # 1)
    # Calcular la suma de todos los elementos en el array

    # suma = ....

    # 2)
    # Calcular la diferencia de todos los elementos en el array

    # diferencia = ....

    # 3)
    # Utilizar la funcion "where" para reemplazar los números múltiplos
    # de "5" por un "0"
    # Ojo: ¿Que operador matematico utilizará para saber si un número es
    # múltiplo de "5"? Ese operador ya lo conoce y lo viene utilizando
    # bastante para saber si un número es múltiplo de "2"

    # nuevo_array = ....
    pass


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    # ej2()
    # ej3()
    # ej4()
    # ej5()
    # ej6()
