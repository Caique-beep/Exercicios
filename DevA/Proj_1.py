"""
1. SIMULADOR DE DADO
Objetivo: Seu script deve gerar um valor aleatório entre 1 e 6(ou uma faixa que você definir)
e permitir que o usuário rode o script quantas vezes quiser
"""
import random

dado = [1, 2, 3, 4, 5, 6]

while True:
    pergunta = input('Você gostaria de girar o dado? ')
    resp = ['sim', 's']
    resp2 = ['nao', 'n', 'não']
    if pergunta.lower() in resp:
        print(random.choice(dado))
    elif pergunta.lower() in resp2:
        print('Obrigado')
        break
    elif pergunta != resp or pergunta != resp2:
        print('Respoda com sim ou não!!!!')
    else:
        break
