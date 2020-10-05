"""
5 Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""


def passei(n1,n2):
    media = float((n1 + n2)) / 2
    if 7 <= media <= 9:
        return print("Aprovado")
    elif media < 7:
        return print("Reprovado")
    elif media == 10:
        return print("Aprovado com Distinção")


passei(10,10)