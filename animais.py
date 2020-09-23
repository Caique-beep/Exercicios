class Gato:
    def __init__(self, tabela):
        self.tavela ={}


    def criar(self, nome: str, idade: int) -> object:
        tabela = {
            'nome': nome,
            'idade': idade,
        }

        return tabela

gato = Gato()
a= gato.criar("tintin", 10)
print(type(a))