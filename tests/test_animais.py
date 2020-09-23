from unittest import TestCase
from animais import Gato


class TestAnimais(TestCase):
    def setUp(self) -> None:
        self.gato = Gato()

    def test_dar_nome_ao_gato(self):
        esperado = {
            'nome': 'Tintin',
            'idade': 10
        }
        result = self.gato.criar('Tintin', 10)
        self.assertEqual(result, esperado)
