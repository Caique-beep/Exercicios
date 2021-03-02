"""
Exercício 10.1
Escreva uma função chamada nested_sum que receba uma lista de listas de números inteiros
e adicione os elementos de todas as listas aninhadas.
"""

a = [1, 2, 3, [4, 1]]


def nested_sum(t):
    total = 0
    for n in t:
        if isinstance(n, list):
            total += sum(n)
        else:
            total = total + n
        print(n)
    return total


print(nested_sum(a))