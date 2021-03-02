"""
Escreva uma função chamada cumsum que receba uma lista de números e retorne a soma cumulativa; isto é,
uma nova lista onde o i-ésimo elemento é a soma dos primeiros i+1 elementos da lista original.
Por exemplo:

''>>> t = [1, 2, 3]
''>>> cumsum(t)
''[1, 3, 6]
"""
t = [1, 2, 3, 4]


def cumsum(t):
    total = 0
    x = []
    for n in t:
        total = total + n
        x.append(total)
        print(x)
    return x


print(cumsum(t))