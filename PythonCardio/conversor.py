"""

Reto 3 - Conversor de millas a kilómetros
Imagina que quieres calcular los kilómetros que son cierta cantidad de millas. Para no estar repitiendo este cálculo 
escribe un programa en que el usuario indique una cantidad de millas y en pantalla se muestre el resultado convertido 
a kilómetros.

Toma en cuenta que en cada milla hay 1.609344 Km

Bonus: haz que el usuario pueda escoger entre convertir millas a kilómetros o kilómetros a millas.

"""

import os

def clear():
    os.system('clear')

def km_to_mis(longitud):
    #Convierte Km a Millas
    return longitud * 0.621371

def mis_to_km(longitud):
    #Convierte Millas a Km
    return longitud / 0.621371


def main():
    clear()
    print('**** Convertidor de KMs a Millas y Millas a KMs **** \n')
    while True:
        try:

            tipo_conversor = int(input('Ingrese 1 - KM a MIS 2 - MIS a KM. Otro número para terminar:  >> '))                        

            if tipo_conversor == 1:
                unidades = float(input('\nIndica las unidades a convertir: >> '))
                print(f'\n{ str(unidades) } km a millas son: { str(km_to_mis(unidades)) } millas\n\n')
            elif tipo_conversor == 2:
                unidades = float(input('\nIndica las unidades a convertir: >> '))
                print(f'\n{ str(unidades) } millas a km son: { str(mis_to_km(unidades)) } km\n\n')
            else:
                break;

            
        except:
            print('Valor incorrecto. Vuelva a ingresar datos.\n')
            continue

if __name__ == "__main__":
    main()