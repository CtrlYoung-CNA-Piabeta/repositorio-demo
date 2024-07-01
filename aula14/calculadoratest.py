import unittest
from calculadora import divisao

class CalculadoraTest(unittest.TestCase):
    def test_divisao(self):
        val = divisao(4, 2)
        self.assertEqual(val, 2)
    
    def test_divisao_division_by_zero(self):
        val = divisao(8, 0)
        self.assertEqual(val, 0)

unittest.main(argv=[''], exit=False)
