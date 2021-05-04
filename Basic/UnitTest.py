import unittest


def suma(numero1, numero2):
    return numero1 + numero2

class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num1 = 10
        num2 = 5

        resultado = suma(num1, num2)
        self.assertEqual(resultado, 15)
        #self.assertNotEqual(resultado, 15)     resultado != 15
        #   .assertGreater          resultado > 15
        #   .assertGreaterEqual     resultado >= 15
        #   .assertLess             resultado < 15
        #   .assertLessEqual        resultado <= 15

    def test_suma_dos_negativos(self):
        num1 = -10
        num2 = -7

        resultado = suma(num1, num2)
        self.assertEqual(resultado, -17)          


if __name__ == '__main__':
    unittest.main(verbosity=2)


"""
   La diferencia entre las pruebas de Caja Negra y Caja de Cristal es que en las pruebas de caja negra se escriben primero los test para ayudarnos a implementar nuevo código. 
   En las pruebas de caja de cristal se asume que se tiene código escrito y las pruebas se escriben para verificar todas las ramificaciones del programa y 
   probar todos los diferentes caminos posibles.

import unittest


def mayor_edad(edad):
    if edad >= 18:
        return True
    else:
        return False


class PruebaDeCristalTest(unittest.TestCase):
    
    def es_mayor(self):
        edad = 15
        result = mayor_edad(edad)

        self.assertEqual(result, True)

    def es_menor(self):
        edad = 100
        result = mayor_edad(edad)

        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()


"""