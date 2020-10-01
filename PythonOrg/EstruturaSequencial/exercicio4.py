"""
9 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""


def convert_temp(val):
    celsius = 5 * ((val - 32) / 9)
    return celsius


a = float(input("Digite a temperatura em Fahrenheit para a conversão em Celsius: "))
b = convert_temp(a)
print("A temperaturq {}F em Celsius fica {}".format(a, b))


"""
10 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
(32 °F − 32) × 5/9 = 0 °C
"""


def celcius_to_f(val):
    F = val * (9 / 5) + 32
    return F


print(celcius_to_f(23))