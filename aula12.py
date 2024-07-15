# Previously on CtrlYoung...
# len
# Set
# variáveis
# git
# listas
# estruturas de repetição (for e while)
# funções
# strings
# estruturas de condição

# POO - Programação Orientada a Objetos
# Classes

class Carro():
    # Propriedades da classe Carro
    velocidade = 0

    # Método Inicializador
    def __init__(self, marca, modelo, cor, portas):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.portas = portas
    
    def __str__(self):
        return f"Este carro é um {self.marca} {self.modelo} {self.cor}"

    # Métodos da classe Carro
    def dar_partida(self):
        print('Sente o ronco do motor!')
    
    def acelerar(self):
        self.velocidade += 100
    
    def frear(self):
        self.velocidade -= 100


# Exemplo 1
# carro1 = Carro()
# carro1.dar_partida()
# carro1.acelerar()
# carro1.acelerar()
# carro1.acelerar()
# print(carro1.velocidade)
# print("Olha o pardal!!!")
# carro1.frear()
# carro1.frear()
# print(carro1.velocidade)

# Atividade 1: Criar uma classe de Animal

# Exemplo 2
# carro2 = Carro()
# print("Carro 1")
# print(carro1.marca)
# print(carro1.modelo)
# print(carro1.cor)
# print("Carro 2")
# print(carro2.marca)
# print(carro2.modelo)
# print(carro2.cor)


# Exemplo 3
carro = Carro('Fiat', 'Uno', 'branco', 6)
gol = Carro('Volkswagen', 'Gol', 'branco', 6)
print(carro.modelo)
print(carro.marca)
print(carro.cor)
print(carro)
print(gol)

# Atividade Final: 
# Criar inicializador para a classe Animal criada


class Animal:
    def __init__(self,_cor, _pelo):
        self.pelo = _pelo 
        self.cor = _cor



# Polimorfismo


