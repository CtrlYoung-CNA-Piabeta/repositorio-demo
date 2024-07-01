import unittest
from pokemon import Pokemon

# TDD => Test Driven Development
class PokemonTest(unittest.TestCase):
    def setUp(self):
        self.pokemon = Pokemon('Charmander', 100)

    def test_recebe_dano(self):
        self.pokemon.recebe_dano(80)
        self.assertEqual(self.pokemon.hp_atual, 20)
    
    def test_recebe_dano_maior_que_hp_atual(self):
        self.pokemon.recebe_dano(101)
        self.assertEqual(self.pokemon.hp_atual, 0)

    def test_curar(self):
        self.pokemon.recebe_dano(80)
        self.pokemon.curar(80)
        self.assertEqual(self.pokemon.hp_atual, 100)

    def test_curar_mais_que_o_maximo(self):
        self.pokemon.recebe_dano(1)
        self.pokemon.curar(9999)
        self.assertEqual(self.pokemon.hp_atual, self.pokemon.hp_maximo)


unittest.main(argv=[''], exit=False)