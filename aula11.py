# Calcular a média em uma lista
# Ex: [ 1, 2, 3, 4, 5 ] = 3
def calcula_media( lista ):
    total = 0.0
    for item in lista:
        total += item
    return total/len(lista)
lista1 = [1, 2, 3, 4, 5]
lista2 = [3.5, 7.7, 2.6]
lista3 = [5, 78, 217, 0.9]
print(calcula_media(lista1))
print(calcula_media(lista2))
print(calcula_media(lista3))