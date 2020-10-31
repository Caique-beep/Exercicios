"""
8 Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
"""

def menor_de_tres(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        return n1
    elif n2 < n1 and n2 < n3:
        return n2
    else:
        return n3


pergunta = float(input("Informe o preço do produto 1: "))
pergunta2 = float(input("Informe o preço do produto 2: "))
pergunta3 = float(input("Informe o preço do produto 3: "))
print("O mais barato entre eles é ", menor_de_tres(pergunta, pergunta2,pergunta3))