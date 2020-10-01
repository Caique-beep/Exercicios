"""
16
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
pergunta = int(input("Quantos metros quadrados será pintado? "))


def tintas_usar(m_quadrados):
    litro = m_quadrados / 3
    return litro


def latas():
    func = tintas_usar(pergunta)
    if func < 0:
        return 1
    latas_de_tinta = round(func / 18) + 1
    print(latas_de_tinta)
    return latas_de_tinta


a = latas()
preco = int(a * 80)
print("Voce deverá comprar {:.0f} latas de tinta e pagará {:.2f} reais".format(a, preco))
