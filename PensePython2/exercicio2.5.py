"""
Escreva uma função chamada middle que receba uma lista e
retorne uma nova lista com todos os elementos originais,
exceto os primeiros e os últimos elementos. Por exemplo:

''>>> t = [1, 2, 3, 4]
''>>> middle(t)
[2, 3]
"""
t = [1, 2, 3, 4]


def middle(t):
    new_list = t[1:-1]
    print(new_list)
    print(type(new_list))
    return new_list

"""
Escreva uma função chamada chop que tome uma lista alterando-a para remover o primeiro 
e o último elementos, e retorne None. Por exemplo:

>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
    [2, 3]
"""


def chop(t):
    del t[0]
    del t[-1]
    print(t)


print(chop(t))