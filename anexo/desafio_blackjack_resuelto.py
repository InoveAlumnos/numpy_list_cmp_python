import random

def blackjack_module():

    print("Ingrese su nombre!")

    nombre = str(input())

    numeros = [random.randint(1, 10) for x in range(2)]

    while sum(numeros) < 21:
        print("Tus cartas:", numeros, " suman:", sum(numeros), " Querés mas? Y/n?\n")

        choice = str(input())

        if choice == 'Y':
            numeros.append(random.randint(1, 10))
        elif choice == 'n':
            break
        else:
            print("ponele voluntad,", nombre, " es Y o n")

    print("Tus cartas:", numeros, " suman:", sum(numeros), "\n")

    if sum(numeros) > 21:
        print("Patinaste como chorizo en fuente de loza")
        resultado = {'puntaje': 0, 'jugador': nombre}
        return resultado

    resultado = {'puntaje': sum(numeros), 'jugador': nombre}

    return resultado

if __name__ == '__main__':

    print('Ingrese acontinuación la cantidad de jugadores...')

    # Crear jugadores
    n_jugadores = int(input())    

    # Empezar juego
    players = [blackjack_module() for x in range(n_jugadores)]

    # Ordenar por puntaje (por ganadores)
    players.sort(reverse=True, key=lambda x: x['puntaje'])

    # Imprimir tabla de ranking
    [print ('*' ,end='') for x in range(45)]
    print('')
    print('Ranking!! :D')
    [print ('*' ,end='') for x in range(45)]
    print('')
    [print('jugador >', x.get('jugador'),'puntaje:', x.get('puntaje')) for x in players]
    [print ('*' ,end='') for x in range(45)]
    print('')
    ranking = [x.get('puntaje') for x in players]

    if n_jugadores > 1:

        if ranking[1] == ranking[0]:
            print('Empate!')

        elif sum(ranking) == 0:
            print('Perdedores!')

        else:
            winner = [x.get("jugador") for x in players if x.get('puntaje') == ranking[0]]
            print('Ganó', winner[0], '!!')

    elif n_jugadores == 0:
        print('Volvé otro día entonces...')

    else:
        if ranking[0] > 0:
           player = [x.get("jugador") for x in players if x.get('puntaje') == ranking[0]]
           print('Ganaste', player[0], '!!')

        else:
           player = [x.get("jugador") for x in players if x.get('puntaje') == ranking[0]]
           print('Perdiste', player[0], '!!')