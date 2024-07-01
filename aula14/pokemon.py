class Pokemon:
    def __init__(self, nome, hp_maximo):
        self.nome = nome
        self.hp_maximo = hp_maximo
        self.hp_atual = hp_maximo

    def recebe_dano(self, dano):
        self.hp_atual -= dano
        if self.hp_atual < 0:
            self.hp_atual = 0
            print(f'{self.nome} foi jogar no Vasco.')

    def curar(self, pv):
        self.hp_atual += pv
        if self.hp_atual > self.hp_maximo:
            self.hp_atual = self.hp_maximo
