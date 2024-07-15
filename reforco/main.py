# Dicionários , tuplas e sets

# Tuplas - Semelhantes às listas, porém não pode ter seu 
# valor alterado.

tup = (5 , 'oi' , True , 2.5 , False , 5 , 5 , 5)

# tup.append(8)
# print(len(tup))
# print(tup.count(5))


# Sets

unico = set()
meu_set = {5 , 2 , 4 , 8, '8'}

unico.add(5)
unico.add(5)

# print(meu_set)

# [] - () - {}
# Dicionário

dic = {
    'nome': 'Wendell',
    'idade': 20,
    'id': 2546,
    'endereço': ['rua: exemplo' , 'numero: 8']
}


if 'nome' in dic:
    print(dic['nome'])

print(dic['endereço'][1])

for chave in dic.keys():
    print(chave)

for valor in dic.values():
    print(valor)

# print(pessoa['nome'])



# Arquivos




# Função recursiva
# def rec(a):
#     if a != 2:
#         print(a , 'é diferente de 2')
#         rec(a + 1)
#     else:
#         return print(a)
    
# rec(0)


# Dada a lista (1,3,2,3,4,5,1,5,7,6,8,3,4), crie uma 
# segunda lista apenas com os itens na mesma ordem, mas 
# sem repetição.