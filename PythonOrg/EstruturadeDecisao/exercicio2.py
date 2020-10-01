"""
3 Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""


def sexo(val):
    if val == "F":
        return "Feminino"
    elif val == "M":
        return "Masculino"
    else:
        return "Sexo inválido"


a = input("Qual é o seu sexo? F para feminino ou M para Masculino: ")
print(sexo(a.upper()))

"""
4 Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""


def isvolgal(letra):
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print('A letra é uma vogal')
    else:
        print('A letra é uma consoante')


c = input("Digite uma letra: ")
print(c)

isvolgal(c)