#!/usr/bin/env python
'''
Numpy [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import numpy as np
import math


def ej1():
    # Lambda expression
    # Realizar una funcion lambda que eleve al cuadrado
    # el número pasado como parámetro
    
    # potencia_2 = lambda......

    # List de string
    numeros = [1, -5, 4, 3]

    # Utilice la función map para mapear una lambda expression
    # que retorne la potencia de 2 de cada numero en la lista numeros
    # El resultado (la potencia de cada numero) se debe ir almacenando
    # en una nueva lista
    # Nota: realizar la lambda expression "in line", es decir,
    # no declarar la lambda fuera del map sino diretamente dentro

    # numeros_potencia = list(map....)


def ej2():
    # Lambda expression
    # Realizar una funcion lambda que retorne el tamaño
    # (len) de un string pasado como parámetro
    
    # len_string = lambda......

    # List de string
    palabras = ['Inove', 'casa', 'programacion']

    # Utilice la función map para mapear una lambda expression
    # que retorne el tamaño (len) de cada texto em cata iteración
    # de la lista de textos
    # El resultado (el len de cada palabra) se debe ir almacenando
    # en una nueva lista
    # Nota: realizar la lambda expression "in line"

    # palabras_len = list(map....)


def ej3():
    # Práctica de compresion de listas
    pass


def ej4():
    # Utilizar compresion de listas con condicionales
    pass


def ej5():
    # Utilizar compresion de listas para filtrar
    pass


def ej6():
    # Ejercicio de funciones Numpy
    # Arme un array con el méotod arange
    # el cual este acotado entre 0 y 1000
    # Dicho array calcular las siguientes operaciones:

    # Calcular la suma de todos los elementos en el array
    
    # suma = ....

    # Calcular la diferencia de todos los elementos en el array
    
    # diferencia = ....

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
    #ej2()
    #ej3()
    #ej4()
    #ej5()
    #ej6()
