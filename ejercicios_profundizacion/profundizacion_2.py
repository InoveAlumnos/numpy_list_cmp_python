# Numpy [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Dado una lista de nombres de personas "nombres" se desea
obtener una nueva lista filtrada que llamaremos "nombres_filtrados"
La lista se debe filtrar por comprensión de listas utilizando la
lista "padron" como parámetro.
La lista filtrada sodo deberá tener aquellos nombres que empiecen
con alguna de las letras aceptadas en el "padron".

TIP: Debe acceder a la primera letra de cada nombre de la lista nombres
y luego utilizar el operador "in" para ver si esta letra existe
dentro de la lista "padron".

IMPORTANTE: Resolver con compresion de listas, pero si resulta muy complejo
es preferible que arranque utilizando los métodos tradicionales
de bucle/condicionales y luego intentarlo con comprension de listas
'''

if __name__ == '__main__':
    print('Comenzamos a ponernos serios!')

    padron = ['A', 'E', 'J', 'T']

    nombres = ['Tamara', 'Marcelo', 'Martin', 'Juan', 'Alberto', 'Exequiel',
               'Alejandro', 'Leonel', 'Antonio', 'Omar', 'Antonia', 'Amalia',
               'Daniela', 'Sofia', 'Celeste', 'Ramon', 'Jorgelina', 'Anabela']

    # A partir de aquí escriba el código que resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda

    # Se espera obtener:
    # ['Tamara', 'Juan', 'Alberto'......]

    print("terminamos")