"""
8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês
"""


def calc_salario(x, y):
    salario = x*y
    return salario


pergunta = float(input("Quanto voce ganha por hora? "))
pergunta_dois = float(input("Quantas horas voce trabalha por mês? "))
result = calc_salario(pergunta, pergunta_dois)
print("O seu salario é de: {}".format(result))