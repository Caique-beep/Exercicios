class Observador:
    def atualizar(self, data):
        ...


class Observavel:

    def __init__(self):
        self.observers = []

    def registrar_observador(self, observer):
        self.observers.append(observer)

    def remover_observador(self, observer):
        self.observers.remove(observer)

    def notificar_observadores(self, data):
        for observer in self.observers:
            observer.atualizar(self, data)


Observavel('caique')