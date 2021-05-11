"""
2. CHUTE O NÚMERO
Objetivo: Criar um script que gerá um valor aleatoriamente, guarda este valor,
e pergunta repetidamente para o usuário chutar o valor gerado até que ele acerte.
"""
import random


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:

    pergunta = input(str('Você gostaria de jogar? '))
    resp = ['sim', 's']
    resp2 = ['nao', 'n', 'não']
    if pergunta.lower() in resp:
        escolha = (random.choice(l1))
        tentativas = []
        while True:
            try:
                valor_do_usuario = int(input("Chute um numero: "))
                len_tent = len(tentativas)
                tentativas.append(valor_do_usuario)
                print("Suas tentativas {}".format(tentativas))
                if escolha == valor_do_usuario:
                    print("**** Parabéns voce acertou número!! ****")
                    break
                elif valor_do_usuario > escolha:
                    print("Você chutou alto")
                elif valor_do_usuario < escolha:
                    print("Você chutou baixo")
                else:
                    print("Tente outra vez")
            except ValueError:
                print('-----Digite um número!!!-----')
    elif pergunta.lower() in resp2:
        print('Obrigado')
        break
    else:
        print("Digite sim ou não!!")


