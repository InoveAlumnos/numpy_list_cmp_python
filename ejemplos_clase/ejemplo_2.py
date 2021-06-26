# Numpy [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
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

    print("terminamos")