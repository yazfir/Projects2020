"""

Reto 1 - Área de un triángulo
Es momento de poner ese conocimiento a la práctica. El área de un triángulo se describe de la siguiente manera: A = (b * h) / 2 .

Escribe un programa que tome la base y la altura como parámetros y calcule el área del triángulo.

Bonus: el programa debe determinar si el triángulo es isósceles, equilátero o escaleno.

"""

import math

def area(lado_a, lado_b, lado_c):
    """ Área de un triángulo aplicando fórmula de Herón """
    semi = (lado_a + lado_b + lado_c) / 2    #semiperímetro
    return math.sqrt( semi * (semi - lado_a) * (semi - lado_b) * (semi - lado_c))

def tipo(lado_a, lado_b, lado_c):
    """ Obtenemos el tipo de triángulo ingresado. """
    if(lado_a == lado_b and lado_a == lado_c):
        print('Los datos ingresados son de un triángulo equilátero.')
    elif(lado_a != lado_b and lado_a != lado_c and lado_b != lado_c):
        print('Los datos ingresado son de un triángulo escaleno.')
    else:
        print('Los datos ingresado son de un triángulo isóceles.')


def main():

    print('**** Tipo de triángulo y su área con 3 valores ****')
    a = float(input('Ingresa la medida del 1er. lado: '))
    b = float(input('Ingresa la medida del 2d0. lado: '))
    c = float(input('Ingresa la medida del 3er. lado: '))

    tipo(a,b,c)
    print(f'El área del triángulo con los datos propocionados es: { area(a,b,c) }')

if __name__ == '__main__':
    main()