# # Resumo 

# class Pessoa:
#     __dinheiro = 0
#     fome = True
    
#     def __init__ (self, _nome, _genero, _idade):
#         self.nome = _nome
#         self.genero = _genero
#         self.idade = _idade

#     def __str__ (self):
#         return f'Nome: {self.nome}'

#     def setTrabalhar(self, salario):
#         self.__dinheiro += salario

#     def getDinheiro(self):
#         return self.__dinheiro

#     def setComer(self):
#         self.fome = False

#     def getFome(self):
#         return self.fome

# # Setters - Getters

# felipe = Pessoa('Felipe', 'hetero', 17)

# print(felipe)

# felipe.setTrabalhar(200000)
# print(felipe.dinheiro)


class Animal:
    def __init__(self):
        print('Animal Criado')
    
    def oQueE(self):
        print('Animal')

    def comer(self):
        print('Comendo...')

# Herança
class Abelha(Animal):
    def __init__(self):
        print('Abelha Criado')
    
    def oQueE(self):
        print('Abelha')

    def bzz(self):
        print('Bzzz')

abelha = Abelha()
abelha.comer()