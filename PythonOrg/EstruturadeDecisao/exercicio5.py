"""
8 Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
"""


def maior_e_menor(n1, n2, n3):
    l = [n1, n2, n3]
    l.sort()
    a = l[0]
    return "O mais barato entre eles é {} ".format(a)


pergunta = float(input("Informe o preõ"))


dicct = {}
