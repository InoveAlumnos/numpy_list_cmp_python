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
Se dispone del diccionario "producto" que se utiliza para
traducir el número ID de un producto en su nombre, por ejemplo:

producto 556070 --> nombre 'Auto'

Por otro lado se dispone de la lista de productos comprados "lista_compra_id"
por un cliente con sus códigos de productos

Alumno, su objetivo es crear una lista nueva "lista_compra_productos" 
que sea la transformación de la lista "lista_compra_ida",
que en vez de estar tener los "ID" de los productos tenga el "nombre"
de cada producto según su id.

1) Iterar sobre la lista "lista_compra_id" para generar la nueva
utilizando comprension de listas como generador

2) En cada iteración acceder al diccionario para traducir el ID
a nombre de producto

NOTA: Tener en cuenta que puede haber códigos (IDs) que
no esten registrados en el sistema, en esos casos se debe
almacenar en la lista la palabra 'NaN', para ello puede hacer uso
de condicionales PERO recomendamos leer atentamente el método "get"
de diccionarios que tiene un parametro configurable respecto
que sucede sino encuentra la "key" en el diccionario.

NOTA: Esta información bien podría ser una tabla SQL: id | producto
de una base de datos como veran más adelante.
Tambien se lo conoce como el proceso de transformar variable numéricas en categóricas
en análisis de datos.
'''

if __name__ == '__main__':
    print("Acercamiento al uso de datos relacionales")

    producto = {
                556070: 'Auto',
                704060: 'Moto',
                42135: 'Celular',
                1264: 'Bicicleta',
                905045: 'Computadora',
                }

    lista_compra_id = [556070, 905045, 42135, 5674, 704060, 1264, 42135, 3654]

    # A partir de aquí escriba el código que resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda


    print("terminamos")