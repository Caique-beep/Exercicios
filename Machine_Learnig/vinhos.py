import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier

arquivo = pd.read_csv(r'C:/Users/caiqu/dataset_vinhos.csv.csv')

arquivo.head()

arquivo['style'] = arquivo['style'].replace('red', 0)
arquivo['style'] = arquivo['style'].replace('white', 1)
print(arquivo)

# Separando as variaveis em preditoras e alvo
y = arquivo['style']  # alvo
x = arquivo.drop('style', axis=1)  # todo o resto
"""
A variavel X recebe toda a tabela exceto a coluna style
"""

"""
Criando conjuntos de treino e teste
"""
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)#test size é = a porcentagem de vai pra teste 30%

modelo = ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)#fit é uma função do EXtra que aplica o algoritimo Extra nos dados

resultado = modelo.score(x_teste, y_teste)#para fazer a verificação do algoritimo

#print("Acuracia:",resultado)