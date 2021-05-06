import matplotlib.pyplot as plt
import numpy as np


def funcion(x):
  return 2*x**8 - x**4 + 3*x**2 + 4

def main():
 
    res = 100

    x = np.linspace (-10.0, 10.0, num=res)

    y= funcion(x)

    fig, ax = plt.subplots()

    ax.plot(x,y)
    ax.grid()
    ax.axhline(y=0, color ='r')
    ax.axvline(x=0, color = 'r')
    plt.xlim(-5, 5)
    plt.ylim(0, 20)
    plt.show() 


if __name__ == '__main__':
    main()