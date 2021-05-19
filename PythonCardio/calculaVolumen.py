"""

Reto 4 - Calculadora de volúmenes
Sigamos con matemáticas elementales para no perder la costumbre y retar nuestras habilidades. 
Escribe un programa donde apliques las diferentes fórmulas matemáticas para calcular el volumen de un cilindro.

Recuerda que la base del cilindro es un círculo y necesitarás calcular su área. Aplica las fórmulas en tu programa 
recibiendo datos como altura y radio.

Bonus: agrega otras figuras geométricas a tu programa y que el usuario pueda escoger cuál calcular.

"""

import math
import os

def clear():
    os.system('clear')

def vCubo():
    print('\n\n**** Volumen Cubo ****')
    longitud = float(input('Ingresa la longitud de una de sus caras >> '))
    print(f'El volumen del cubo es: { str(longitud**3) }')

def vCilindro():
    print('\n\n**** Volumen Cilindro ****')
    radio = float(input('Ingresa el valor del radio >> '))
    altura = float(input('Ingresa el valor de la altura >> '))
    print(f'El volumen del cilindro es: { str(math.pi * radio**2 * altura) }')

def menu():
    while True:

        try:
            return int(input('Indica el valor del volumen a calcular: 1 - Cubo 2 - Cilindro  3 - Otro número para salir >>  '))
        except:
            print('Valor no válido.')
            continue

def main():
    volumenes = [vCubo, vCilindro]
    clear()
    print('**** Calculando Volumenes ****')
    while True:
        opcion = menu()
        if opcion in [1, 2]:
            volumenes[opcion-1]()
        else:
            break;


if __name__ == '__main__':
    main()