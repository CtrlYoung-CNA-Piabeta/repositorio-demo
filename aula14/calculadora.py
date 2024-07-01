# 1. Criar classe calculadora com as funções de soma, subtração, multiplicação e divisão
# 2. Criar classe de teste para essa classe
# 3. Utilizar try except na classe

def divisao(numerador, denominador):
    try:
        resultado = numerador / denominador
        return resultado
    except ZeroDivisionError as e:
        print("Oh, não vai dar não! Divisão por zero não rola!")
        print(e)
    except TypeError:
        print("Oh, tu tá usando o tipo errado! Tem que usar inteiro ou float.")
    finally:
        print("Divisão concluída.")

# print(divisao(2, 3))
# print(divisao(1, 137))
# print(divisao(1, 0))
# print(divisao(1, '1'))

try:
    file = open('teste.txt', 'r')
    file.write('Choque do trovão!')
except Exception as e:
    print(e)