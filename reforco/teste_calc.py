import unittest

class Calculadora:
    def soma(self, a ,b):
        return a + b
    
    def subtracao(self, a ,b):
        return a - b
    
class TesteCalculadora(unittest.TestCase):
    def setUp(self):
        self.c = Calculadora()

    def test_soma(self):
        self.assertEqual(self.c.soma(5 , 5), 10)

    def test_subtracao(self):
        self.assertEqual(self.c.subtracao, 0)

unittest.main(argv=[''], exit=False)