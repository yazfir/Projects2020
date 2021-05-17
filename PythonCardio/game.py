"""

Reto 2 - Piedra, papel o tijera
Este es un juego en el que nunca fui bueno, pero eso no significa que hacer un programa sea difícil. 
Escribe un programa que reciba como parámetro “piedra”, “papel”, o “tijera” y determine si ganó el jugador 1 o el jugador 2.

Bonus: determina que el ganador sea el jugador que gane 2 de 3 encuentros.

Ejemplo:

ppt(“piedra”, “papel”) ➞ “El ganador es el jugador 2

"""

import random

def winner(player1, player2):
    #Determina ganador de juego piedra-papel-tijera
    if(player1 == player2):
        return 'Empate'
    elif (player1 == 'PIEDRA 👊' and player2 == 'TIJERA ✌') or (player1 == 'PAPEL ✋' and player2 == 'PIEDRA 👊') or (player1 == 'TIJERA ✌' and player2 == 'PAPEL ✋'):
        return 'Humano'
    else:
        return 'Computador'


def main():
    # 2 PIEDRA --> TIJERA
    # 1 TIJERA --> PAPEL
    # 0 PAPEL --> PIEDRA
    respuesta = 1
    Jugadas = ['PIEDRA 👊','PAPEL ✋','TIJERA ✌']
    num_juegos = 3
    iteraciones = 0
    wins1 = 0
    wins2 = 0

    print('\n\n**** Juego Piedra--Papel--Tijera ****')
    print('Este es un duelo contra el computador. El ganador es el primero en obtener 2 victorias de N juegos.\n')

    while iteraciones < num_juegos:
        
        respuesta = int(input('\nIndica el número correspondiente a tu jugada: 1-PIEDRA 👊 2- PAPEL ✋ 3-TIJERA ✌  : '))
        if respuesta in [1,2,3]:
            iteraciones += 1
            player1 = Jugadas[respuesta -1]    
            player2 = Jugadas[random.randint(0,2)]
            ganador = winner(player1,player2)
            print(f'Jugada Humano: {player1} vs Jugada Computador: {player2} ===>>  ({player1} vs {player2})\n')
            print(f'Esta partida la gana : { ganador } \n')
            if ganador == 'Empate':
                iteraciones -= 1
            elif ganador == 'Humano':
                wins1 += 1
                if wins1 == 2:
                    print('\n El ganador final es: Humano')                
                    break
            else:
                wins2 += 1
                if wins2 == 2:
                    print('\n El ganador final es: Computador')
                    break
            
        else:
            print('\nValor ingresado incorrecto. Ingrese valor válido.\n')


if __name__ == "__main__":
    main()