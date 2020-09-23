"""
Exercício 3.3
Nota: Este exercício deve ser feito usando-se apenas as instruções e os outros recursos que aprendemos até agora.

Escreva uma função que desenhe uma grade como a seguinte:
        + - - - - + - - - - +
        |         |         |
        |         |         |
        |         |         |
        |         |         |
        + - - - - + - - - - +
        |         |         |
        |         |         |
        |         |         |
        |         |         |
        + - - - - + - - - - +
Dica: para exibir mais de um valor em uma linha, podemos usar uma sequência de valores separados por vírgula:

print('+', '-')
Por padrão, print avança para a linha seguinte, mas podemos ignorar esse comportamento e inserir um espaço no fim,
desta forma:

print('+', end=' ')
 print('-')
A saída dessas instruções é + -. Uma instrução print sem argumento termina a linha atual e
vai para a próxima linha.

Escreva uma função que desenhe uma grade semelhante com quatro linhas e quatro colunas.
"""


def do_twice(func, arg):
    func(arg)
    print_spam()
    func(arg)
    print_spam()
    func(arg)


def print_spam():
    print(' /', ' '*6, ' /', ' '*6, ' /')
    print(' /', ' '*6, ' /', ' '*6, ' /')
    print(' /', ' '*6, ' /', ' '*6, ' /')
    print(' /', ' '*6, ' /', ' '*6, ' /')


def print_twice(bruce):
    print(bruce*2, '+')


def do_four(func, arg):
    do_twice(func, arg)


do_four(print_twice, arg=' + - - - -')