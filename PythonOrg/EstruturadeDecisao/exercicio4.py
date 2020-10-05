"""
6 Faça um Programa que leia três números e mostre o maior deles.
"""


def maior_de_tres(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3


print(maior_de_tres(10, 5, 2))

"""
7 Faça um Programa que leia três números e mostre o maior e o menor deles.
"""


def maior_e_menor(n1, n2, n3):
    l = [n1, n2, n3]
    l.sort()
    a = l[0]
    b = l[-1]
    return "O menor entre eles é {} e o maior é {}".format(a, b)


print(maior_e_menor(10,15,3))