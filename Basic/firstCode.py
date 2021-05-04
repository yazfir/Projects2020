""" 
    En python las variables no pueden empezar con el 1 (uno), sólo A, a, 2-0, _ (guión bajo)

    if ... elif ... elif ... elif ... else ...

    pass - palabra reservada que se usa para asignar a una función que aun no tiene internamente código

"""

def main():
    #saludoInicial()
    #Aritmetica()
    #Variables()
    #Cadenas()
    #EntradasDatos()
    #CondicionyComparativa()
    #Iteraciones()
    #IteracionesFor()
    #Enumeraciones()
    #Aproximacion()
    #BusquedaBinaria()
    #ScopeOrAlcance()
    #Tuplas()
    #Rangos()
    #Listas()
    Diccionarios()



def saludoInicial():
    print('Hello world!')    
    a=5+3
    print ("Resultado de A es:" + str(a))

def Aritmetica():
    print(5*"hola")
    print(5**3)

def Variables():
    base = 2
    altura=4
    area=(base*altura)/2
    print("Area:"+str(area))

def Cadenas():
    print("Esto es " + "Concatencion")
    #funciones len "longitud"
    my_str="rifzay"
    print(len(my_str))
    print(my_str[0]) # r
    print(my_str[1]) # i
    print(my_str[2]) # f
    print(my_str[2:]) # fzay    - inicia en 2 hasta el final
    print(my_str[:3]) # rif     - desde el incio hasta la posición 3
    print(my_str[:-2]) #rifz    - desde el inicio hasta el final -2
    print(my_str[::2]) #rfa     - desde el inicio y cada 2 posiciones

    print(f"Otra forma de concatenar: {my_str}")

def EntradasDatos():
    nombre=input('¿Cuál es tu nombre?: ') #Las entradas siempre son de tipo String
    print(f'Tú nombre es {nombre}')

    edad=int(input('¿Cuál es tu edad?: '))
    print(f'Tú nombre es {edad}')

def CondicionyComparativa():
    num1=int(input('Ingresa un primer numero entero: '))    
    num2=int(input('Ingresa un primer numero entero: ')) 

    if num1 > num2:
        print('num1 es mayor num2')
    elif num1 < num2:
        print('num1 es menor num2')
    else:
        print('Los números son iguales')

def Iteraciones():
    #while
    contador=0
    while contador < 10:
        print(contador)
        if contador == 4:
            break

        contador+=1

def IteracionesFor():
    frutas = ['manzana', 'pera', 'mango']
    for fruta in frutas:
        print(fruta)

    #iter('fruta') # cadena
    #iter(['a', 'b', 'c']) # lista
    #iter(('a', 'b', 'c')) # tupla
    #iter({'a', 'b', 'c'}) # conjunto
    #iter({'a': 1, 'b': 2, 'c': 3}) # diccionario


    iterador = iter(frutas)
    print(next(iterador)) #manzana
    print(next(iterador)) #pera
    print(next(iterador)) #mango
    #print(next(iterador)) #Error StopIteration

    estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
    }

    for pais in estudiantes:
        print(f'Pais (1er Valor): {pais} \n')

    for pais in estudiantes.keys():
        print(f'Pais (Keys): {pais} \n')

    for numero_de_estudiantes in estudiantes.values():
        print(f'Num Estudiantes (Values): {numero_de_estudiantes} \n')

    for pais, numero_de_estudiantes in estudiantes.items():
        print(f'ITEMS: Pais: {pais} -- Num Estudiantes: {numero_de_estudiantes} \n')


def Enumeraciones():
    objetivo = int(input('Escoge un entero: '))
    respuesta = 0

    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta+=1


    if respuesta**2 == objetivo:
        print(f'La raíz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene un raíz cuadrada exacta')

def Aproximacion():
    objetivo = int(input('Escoge un entero: '))
    epsilon = 0.01
    paso= epsilon ** 2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(respuesta)
        respuesta += paso


    if abs(respuesta**2 - objetivo) >= epsilon :
        print(f'No se encontró la raíz cuadrada de {objetivo}')
    else:
        print(f'La raíz cuadrada de {objetivo} es {respuesta} ')   

def BusquedaBinaria():
    objetivo = int(input('Escoge un entero: '))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)                 
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        
        print(f'respuesta**2={respuesta**2}, abs(x)={abs(respuesta**2-objetivo)}')
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta} /n')
        
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta} /n')
        print(f'respuesta**2={respuesta**2}, abs(x)={abs(respuesta**2-objetivo)}')

    print(f'La raíz cuadrada de {objetivo} es {respuesta}')

def ScopeOrAlcance():

    def func1(un_arg, una_func):
        def func2(otro_arg):
            return otro_arg * 2
        
        valor = func2(un_arg)
        return una_func(valor)

    un_arg = 1

    def cualquier_func(cualquier_arg):
        return cualquier_arg + 5

    resultado = func1(un_arg, cualquier_func)
    print(resultado)


def Tuplas():
    
    my_tuple = ()
    print(type(my_tuple))

    # A las tuplas puede reasignar la tupla pero nunca modificar su contenido o agregar mas información al mismo

    my_tuple = (1, 'dos', True)

    print(my_tuple[0])
    print(my_tuple[1])

    #my_tuple[0] = 2 # Error

    """
        Si asignamos un entero a la variable, lo tomara como tal:       my_tuple = (1)  => <class 'int'>
        Si lo queremos asignar como tupla se debe hacer de esta forma:  my_tuple = (1,) => <class 'tuple'>

    """

    my_tuple = (1,)
    my_other_tuple = (2,3,4)
    my_tuple += my_other_tuple
    print(my_tuple)

    #Se pueden asignar valores a variables de manera consecuente desde una tupla

    x, y, z = my_other_tuple
    print(x)
    print(y)
    print(z)

    #Podemos usar las tuplas para regresar varios valores en un método o función ejem. return (2,'hola', True)    

def Rangos():
    #range(inicio, fin, pasos)

    my_range = range(1,5)
    for i in my_range:
        print(i)        #No inclusivo, el último valor no esta incluido.
    
    my_range = range(0,7,2)
    my_other_range = range(0,8,2)

    print(my_range == my_other_range) # True

    print(id(my_range)) #para saber direccion de memoria utilizado
    print(id(my_other_range))

    print(my_range is my_other_range) #False  - Comparando si es el mismo objeto


def Listas():
    my_list=[1,2,3]

    print(my_list[0])
    print(my_list[1:])

    my_list.append(4)
    print(my_list)

    my_list[0] = 'a'
    print(my_list)

    my_list.pop()
    print(my_list)

    for element in my_list:
        print(element)

    #Posibles efectos colaterales

    a = [1,2,3]
    b = a

    print(b is a) # True  - Es el mismo objeto

    c = [a,b]

    print(c)    # [[1, 2, 3], [1, 2, 3]]

    a.append(5)

    print(a)  # [1, 2, 3, 5]
    print(c)  # [[1, 2, 3, 5], [1, 2, 3, 5]]

    #CLONACION

    d = list(a)     # Con esta función hacemos que sean objetos diferentes
    e = a[::]       # Otra forma de clonar "a" y sean objetos diferentes

    #List Comprehensions

    my_list = list(range(100))
    print(my_list)

    double = [i * 2 for i in my_list]
    print(double)

    pares = [i for i in my_list if i % 2 == 0]
    print(pares)


def Diccionarios():
    my_dic = {
        'David': 35,
        'Erika': 32,
        'Jaime': 50,
    }

    print(my_dic['David']) # 35
    #print(my_dic['Erik']) # Error
    print(my_dic.get('Erik','Error'))
    print(my_dic.get('Jaime','Error'))

    my_dic['Jaime'] = 20
    print(my_dic['Jaime'])

    del my_dic['Jaime']

    for llave in my_dic.keys():
        print(llave)

    for valor in my_dic.values():
        print(valor)

    for llave, valor in my_dic.items():
        print(llave, valor)

    
    print('David' in my_dic) #True
    print('Tom' in my_dic) #False

    """
        Examples dictionary comprehension

        dict_items([('c', 3), ('d', 4), ('a', 1), ('b', 2)])
        dict_variable = {key:value for (key,value) in dictonary.items()}

        dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        double_dict1 = {k:v*2 for (k,v) in dict1.items()}

        dict1_keys = {k*2:v for (k,v) in dict1.items()}  ==>>  {'dd': 4, 'ee': 5, 'aa': 1, 'bb': 2, 'cc': 3}

    """

if __name__ == '__main__':
    main()
