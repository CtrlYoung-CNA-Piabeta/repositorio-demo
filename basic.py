# # String

# nome = 'Wendell'

# # int

# idade = 20

# # Float

# salario = 1500.00

# # Boolean

# verdadeiro = True


# def mostrar_nome(nome):
#     print(nome)

# mostrar_nome('wendell')


# lista_numeros = [1 ,2 ,5 , 5 , 'oi' , True,  2.5]

# print(lista_numeros[0])

# dicionario = {
#     'estado': 'Rio de Janeiro',
#     'ddd': 21,
#     'municipios': ['Magé', 'Rio de Janeiro' ]  
# }

# print(dicionario['municipios'][0])

# # for item in dicionario.values():
#     # print(item)

# # for numero in range(0 , 10):
#     # print(numero)

# idade = int(input('Digite sua idade'))


# def cria_lista(limite):
#     for item in range(0 , limite + 1):
#         print(item)


# x = int(input('Digite um numero'))
# cria_lista(x)

with open('./teste.txt', 'a', encoding = 'utf8' ) as arquivo:
    print(arquivo.write('\n Teste '))