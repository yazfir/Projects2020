import numpy as np
import matplotlib.pyplot as plt

def g(x):
  return x**2

def f(x):
  return np.sin(x)

x = np.linspace(-10,10, num=1000)

f_o_g = f(g(x))
f = f(x)
g = g(x)

#SUBPLOTS(NROWS=1,NCOLS=1, ,DPI=100):CREA UN CONJUNTO DE FIGURAS
#DPI:RESOLUCION DE LA FIGURA
#FIGSIZE(ANCHO=6.4, ALTO=4.8):ANCHO Y ALTO EN PULGADAS
#RETORNA FIGURE, AXES
fig,ax = plt.subplots(3,1,figsize=(14,8),dpi=70)
fig.subplots_adjust(hspace=0.5, wspace=0.5)

ax[0].plot(x,f, linestyle='--', color='green')
ax[0].axhline(y=0, color='r')
ax[0].axvline(x=0, color='r')
ax[0].grid()

ax[1].plot(x,g, linestyle=':', color='blue')
ax[1].axhline(y=0, color='r')
ax[1].axvline(x=0, color='r')
ax[1].grid()

ax[2].plot(x,f_o_g, linestyle='-', color='black')
ax[2].axhline(y=0, color='r')
ax[2].axvline(x=0, color='r')
ax[2].grid()

plt.show()