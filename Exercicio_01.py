from itertools import combinations

"""
    Faça uma combinatória
    ex:
        entrada:[ 1, 2, 3, 4]
        saida:[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4],[3, 4]]

"""

lista = [0, 1, 2, 3, 4]
print(list(combinations('1234', 2)))
# o list é um parametro para fazer a listagem de coisas, já é resevado de python
print(list(combinations(lista, 2)))
