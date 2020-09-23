"""
Escreva uma função chamada square que receba um parâmetro chamado t, que é um turtle.
Ela deve usar o turtle para desenhar um quadrado.
 """
import turtle
import math

bob = turtle.Turtle()


def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
    turtle.mainloop()
    ...


# square(t=bob)

"""
Acrescente outro parâmetro, chamado length, ao square. 
Altere o corpo para que o comprimento dos lados seja length e 
então altere a chamada da função para fornecer um segundo argumento. Execute o programa novamente. 
Teste o seu programa com uma variedade de valores para length.
"""


def square2(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()
    ...


# square2(t=bob, length=150)


"""
Faça uma cópia do square e mude o nome para polygon. 
Acrescente outro parâmetro chamado n e altere o corpo para que desenhe um polígono regular de n lados.
Dica: os ângulos exteriores de um polígono regular de n lados são 360/n graus.
"""


def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)


# polygon(t=bob, length=50, n=7)

"""
Escreva uma função chamada circle que use o turtle, t e um raio r como parâmetros
e desenhe um círculo aproximado ao chamar polygon com um comprimento e número de lados adequados. 
Teste a sua função com uma série de valores de r.
Dica: descubra a circunferência do círculo e certifique-se de que length * n = circumference.
"""





def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


def circle(t, r):
    arc(t, r, 360)


circle(t=bob, r=100)
