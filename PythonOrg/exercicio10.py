"""
17
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
pergunta = int(input("Quantos metros quadrados será pintado? "))


def tintas_usar(m_quadrados):
    litro = m_quadrados / 6
    print(litro)
    return litro


def latas():
    func = tintas_usar(pergunta)
    if func < 0:
        return 1
    latas_de_tinta = round(func / 18) + 1
    return latas_de_tinta


def galao():
    func = tintas_usar(pergunta)
    if func < 0:
        return 1
    galoes_de_tinta = round(func / 3.6) + 1

    return galoes_de_tinta


def real_lata():
    func = tintas_usar(pergunta)
    tinta_lata = round(func/18) + 1
    tinta_galao = round(func/3.6) + 1
    return tinta_lata+tinta_galao

lata = latas()
preco_latas = int(lata*80)
gala = galao()
preco_galao = int(gala*25)
print("Voce deverá comprar {} latas de tinta e pagará {:.1f} R$ "
      "ou comprar {} galões e pagará {:.1f} R$".format(lata, preco_latas, gala, preco_galao))



print(real_lata())