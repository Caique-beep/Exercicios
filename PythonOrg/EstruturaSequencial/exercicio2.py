"""
5 Faça um Programa que converta metros para centímetros.
6 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
import math


def convert_cm(val):
    return val * 100


a = int(input("Insira um numero em metros para ser convertido em cm: "))
b = convert_cm(a)
print("O valor em centimetros é :{}".format(b))


def calc_area(val):
    area = math.pi*(val**2)
    return area


c = int(input("Insira o valor do raio para calcular sua área: "))
d = calc_area(c)
print("A área do circulo com raio {} é de: {}".format(c, d))

"""
7 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""

 
def area_quadrado(val):
    area = val * val
    return area*2