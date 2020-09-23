"""
12 Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
"""


def peso_ideal(altura: float) -> float:
    peso = (72.7 * altura) - 58
    return peso


print(peso_ideal(1.85))

"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""


def peso_ideal2(h: float) -> float:
    global peso
    pergunta = input("Voce é homem ou mulher? ")
    if pergunta == 'homem':
        peso = (72.7 * h) - 58
    elif pergunta == 'mulher':
        peso = (62.1*h) - 44.7
    return peso


print(peso_ideal2(1.85))