"""

En un espacio bidimensional y matemáticamente un recta se define de esta manera:

    y = W0 + W1 x

Donde:

    W0 - Termino Independiente que nos muestra a que altura de la recta corta el eje Y. (Una constante)
    W1 x - La pendiente de la recta, que gráficamente define la inclinación de la recta y conceptualmente cuál es la relación entre
            la variable de entrada X y la variable de salida Y.

Regresión Lineal Simple (RLS)

    Y - Variable Dependiente
    X - Variable Independiente

    Método de Mínimos Cuadrados (W1)

       [ E (X - |X|)(Y - |Y|) ] / [ E (X - |X|)^2 ]

       Donde:

            E :         Sumatoria
            |X|,|Y| :   Media de X o Y
            ^2 :        Al cuadrado

** Instalación matplotlib

        sudo apt-get install python3-matplotlib

"""
import matplotlib.pyplot as plt
import numpy as np

def Operaciones(Valores):
    """ Realiza primeras operaciones de mínimos cuadrados. """
    
    suma = 0.0
    media = 0.0
    
    for valor in Valores:
        suma += valor
    
    media = suma / len(Valores)

    resta = 0.0

    for valor in Valores:
        resta = valor - media
        resta = round(resta,2)
        print(f'X o Y = {valor}, Media = {media}, Resta = {resta}')


def main2():
    DatosX = (1,2,3,4,5)
    DatosY = (2,3,5,6,5)
    Operaciones(DatosX)
    Operaciones(DatosY)
    

def main3():

    x = [1,2,3,4,5]  #[5,7,8,7,2,17,2,9,4,11,12,9,6]
    y = [2,3,5,6,5]  #[99,86,87,88,111,86,103,87,94,78,77,85,86]

    plt.scatter(x, y)
    plt.show()

def main():
    x = np.array([1,2,3,4,5])
    y = np.array([2,3,5,6,5])

    #creamos una matriz al reescribir la ecuacion y=b0+b1x , como y = Ap donde A = [[x] , p = [[b1], [b0]]:

    A = np.vstack([x, np.ones(len(x))]).T

    #aplicamos el metodo de minimos cuadrados de numpy:

    b1, b0 = np.linalg.lstsq(A, y, rcond=None)[0]

    _ = plt.plot(x, y, 'o', label='Original data', markersize=10)
    _ = plt.plot(x, b1*x + b0, 'r', label='Fitted line')
    _ = plt.legend()
    print("Los valores b0 = {}, b1 ={}".format(b0, b1))
    plt.show()    

if __name__ == '__main__':
    main()