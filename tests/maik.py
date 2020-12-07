def test(n):
    i = 1
    while i * (i + 1) * (i + 2) < n:
        i = i + 1
    if i * (i+1) * (i+2) == n:
        print('O numero {} é triangular'.format(n))
    else:
        print('O numero {} não é trinagular'.format(n))


while True:
    try:
        pergunta = int(input("Digite um numero: "))
        break
    except ValueError:
        print('Digite um numero inteiro!')
test(pergunta)

