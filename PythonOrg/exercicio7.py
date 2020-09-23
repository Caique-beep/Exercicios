"""
14 João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e
na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.
"""


def pescador(peso: float):
    global multa
    peso_sp = 50
    peso_excedente = peso - peso_sp
    if peso > peso_sp:
        multa = float(peso_excedente)*float(4.00)
        mensag = print("Devido {} quilos acima do limite, o valor da multa será de: {}".format(peso_excedente, multa))
        return mensag
    elif peso < peso_sp:
        return print("O peso do seu peixe está dentro do limite")


texto = float(input("Quantos quilos deu seu peixe? "))
pescador(texto)
