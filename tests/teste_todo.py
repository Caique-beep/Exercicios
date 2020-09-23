from unittest import TestCase
from app.todo_list import nova_tarefa, process_data
from datetime import datetime


class Test_todo_list(TestCase):
    def test_conseguir_criar_uma_atividade(self):
        esperado = {
            'id': 1,
            'nome': 'Ler um livro',
            'data' : datetime(2020, 7, 17, 0, 0, 0),
            'status' : '????'
        }
        resultado = nova_tarefa('Ler um livro', '17/07/2020')
        self.assertEqual(esperado, resultado)


class TestProcessData(TestCase):
    def test_processar_a_data(self):
        """
        17/07/2020 -> datetime(2020, 07, 17, 0, 0, 0)
        """
        esperado = datetime(2020, 7, 17, 0, 0, 0)
        resultado = process_data('17/07/2020')
        self.assertEqual(esperado, resultado)
