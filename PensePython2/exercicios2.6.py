"""
Escreva uma função chamada is_sorted que tome uma lista como parâmetro e
retorne True se a lista estiver classificada em ordem ascendente,
e False se não for o caso. Por exemplo:

 is_sorted([1, 2, 2])
True
 is_sorted(['b', 'a'])
False
"""
t = [1, 2, 3]


def is_sorted(t):
    return t == sorted(t)

print(is_sorted(t))