import unittest  
from calculadora import calculadora  
  
class TestCalculadora(unittest.TestCase):  
    def teste_soma(self):  
        self.assertEqual(calculadora.soma(2, 3), 5)  
        self.assertEqual(calculadora.soma(-2, 3), 1)  
        self.assertEqual(calculadora.soma(0, 0), 0)  
  
def teste_subtracao(self):  
    self.assertEqual(calculadora.subtracao(5, 3), 2)  
    self.assertEqual(calculadora.subtracao(-5, 3), -8)  
    self.assertEqual(calculadora.subtracao(0, 0), 0)  
  
def teste_multiplicacao(self):  
    self.assertEqual(calculadora.multiplicacao(2, 3), 6)  
    self.assertEqual(calculadora.multiplicacao(-2, 3), -6)  
    self.assertEqual(calculadora.multiplicacao(0, 0), 0)  
  
def teste_divisao(self):  
    self.assertEqual(calculadora.divisao(6, 2), 3)  
    self.assertEqual(calculadora.divisao(-6, 2), -3)  
    self.assertEqual(calculadora.divisao(0, 2), 0)  
  
def teste_operador_invalido(self):  
    with self.assertRaises(ValueError):  
        calculadora.calcula(2, 3, 'x')  
  
def teste_numeros_invalidos(self):  
    with self.assertRaises(ValueError):  
        calculadora.calcula('a', 3, '+')
  
if __name__ == '__main__':  
    unittest.main()