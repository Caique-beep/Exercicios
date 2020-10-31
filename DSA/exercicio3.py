"""
Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os
atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.
"""


class Smartphone():

    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface


class Mp3player(Smartphone):
    def __init__(self, capacidade, tamanho = "Pequeno", interface = "led"):
        self.capaciade = capacidade
        Smartphone.__init__(self, tamanho, interface)

    def print_celular(self):
        print("Celular criado: Tamanho {}, interface {}, capacidade {} GB"\
              .format(self.tamanho, self.interface, self.capaciade))


celular = Mp3player(30)
celular.print_celular()