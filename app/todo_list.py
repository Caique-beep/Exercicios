from datetime import datetime
"""
Fazer um To Do list
nome da atividade
dia da atividade
status: ok ou a fazer

"""


def process_data(string_data: str):
    return datetime.strptime(string_data, '%d/%m/%Y')



def nova_tarefa(nome: str, data: str):
    global identificador
    identificador =+ 1
    tarefa = {
        'id': identificador,
        'nome': nome,
        'data': process_data(data),
        'status': '????'
    }
    return tarefa




