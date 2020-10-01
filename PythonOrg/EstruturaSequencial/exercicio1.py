"""
1 Faça um Programa que mostre a mensagem "Alo mundo" na tela.
2 Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
"""
print("Olá mundo")
mensg = input("Insira um numero:")
print("O numero foi:{}".format(mensg))

"""
3 Faça um Programa que peça dois números e imprima a soma.
4 Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""


def soma(x: int, y: int) -> int:
    return x + y


a = int(input("insira um numero: "))
b = int(input("insira outro numero: "))
result = soma(a, b)
print("O soma desses numeros é:{} ".format(result))