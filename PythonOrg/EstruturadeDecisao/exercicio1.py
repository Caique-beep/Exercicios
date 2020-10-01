"""
1 Faça um Programa que peça dois números e imprima o maior deles.
"""


def maior(x, y):
    if x > y:
        return x
    else:
        return y


a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
c = maior(a, b)
print("O maior entre {} e {} é {}".format(a, b, c))


"""
2 Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""

def neg(val):
    if val > 0:
        return 'é positivo'
    else:
        return 'é negativo'

d = int(input("Digite um número: "))
print(neg(d))
