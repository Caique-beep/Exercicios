"""
11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
- o produto do dobro do primeiro com metade do segundo .
- a soma do triplo do primeiro com o terceiro.
- o terceiro elevado ao cubo.
"""
from numbers import Number


def calcular(val: int, val2: int, val3: Number):
    result1 = (val*2)*(val2/2)
    result2 = (val*3)+val3
    result3 = val3**3
    return result1, result2, result3


print(calcular(10,10, 10))