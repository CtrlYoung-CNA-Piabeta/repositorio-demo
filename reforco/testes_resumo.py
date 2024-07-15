import unittest

# Função soma
def soma(a , b):
    return a + b

# Teste da função soma:
class TesteSoma(unittest.TestCase):
    def test_soma(self):
        resultado = soma(5 , 5)
        self.assertEqual(resultado, 10)


unittest.main(argv=[''], exit=False)