"""
Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail.
Use pelo menos 2 métodos especiais na sua classe.
Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos especiais
"""


class Pessoa():
    def __init__(self, nome, cidade, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return 'Nome: ' + self.nome + '. Mora em: ' + self.cidade


user = Pessoa('Caique', 'Barueri', 12131313, 'caique@gmail.com')
print(user)