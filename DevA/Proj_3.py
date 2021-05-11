"""
4. JOGO DE AVENTURA
Objetivo: Crie um jogo que levará o usuário a vários possíveis finais de acordo com
as respostas que forem passadas para ele.
"""
while True:
    pergunta = input(str('Você gostaria de jogar? '))
    resp = ['sim', 's']
    resp2 = ['nao', 'n', 'não']
    if pergunta.lower() in resp:
        print("Bem vindo ao DD")
        classes = ['Mago', 'Guerreiro', 'Assassino']
        personagem = input('Escolha uma classe para seu personagem: {} '.format(classes))
        if personagem.lower() == 'mago':
            armas_mago = ['Cajado', 'Varinha']
            perso_arma = input(f'Escolha uma arma para seu Mago: {armas_mago} ')
        elif personagem.lower() == 'guerreiro':
            armas_guerreiro = ['Machado', 'Espada']
            perso_arma2 = input('Escolha uma arma para de Guerreiro: {} '.format(armas_guerreiro))
        else:
            armas_assassino = ['Adagas', 'Shurikem']
            perso_arma3 = input('Escolha uma arma para seu Assassino: {} '.format(armas_assassino))
        porta = input('Você chegou a porta de um castelo. O quê você vai fazer? Entra ou Foge? ')
        if porta.lower() == 'entro':
            print('Você entrou')
        elif porta.lower() == 'fujo':
            print("Você correu !!!")
            break
    elif pergunta.lower() in resp2:
        print('Obrigado')
        break
    else:
        print("Digite sim ou não!!")