"""

Reto 5 - Rangos cambiantes
Para este reto final juguemos con números. En tu programa pide al usuario ingresar 3 números: un límite inferior, 
un límite superior y uno de comparación.

Si tu número de comparación se encuentra en el rango de los dos límites, imprímelo en pantalla.

En caso de estar por debajo del inferior o arriba del superior, también muéstralo en pantalla y pide ingresar otro número 
para repetir el proceso.

"""

import os

def clear():
    os.system('clear')

def rangos():
    while True:
        try:
            maximo = int(input('\nIngresa un valor máximo entero >> '))
            minimo = int(input('\nIngresa un valor mínimo entero >> '))

            if maximo <= minimo: print('Valor mínimo incorrecto.'); continue

            while True:
                compara = int(input('\nIngresa un valor de comparación entero >> '))
                if maximo >= compara and minimo <= compara:
                    print(f'El número de comparación esta en rango: {str(compara)}\n')
                    break
                else:
                    print(f'El número de comparación no esta en rango: {str(compara)}. Ingresar otro.\n')
                    continue
            break
        except:
            print('Uno de los valores ingresados es incorrecto. Vuelva a ingresar.\n')
            continue


def menu():
    while True:

        try:
            return int(input('Ingresa: 1 - Comenzar 2 - Otro número para salir >>  '))
        except:
            print('Valor no válido.')
            continue

def main():
    clear()
    print('**** Valor dentro de rangos ****')
    while True:
        opcion = menu()
        if opcion in [1]:
            rangos()
        else:
            break;


if __name__ == '__main__':
    main()