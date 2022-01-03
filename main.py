def checarparenteses(expressao):
    cont = 0
    for x in expressao:
        if x == ')' and cont == 0:
            print('incorrect')
            return
        if x == '(':
            cont += 1
        elif x == ')':
            cont -= 1

    if cont == 0:
        print('correct')
    else:
        print('incorrect')

expr = []

n = int(input('Digite a quantidade de expressões (entre 1-10000): '))

if 1 > n or n > 10000:
    while True:
        n = int(input('Valor fora do intervalo permitido! Digite novamente: '))
        if 1 <= n <= 10000:
            break

for i in range(0, n):
    pergNovamente = True
    while pergNovamente:
        expressao = input(f'Digite a {i+1}ª expressão: ')
        if 0 < len(expressao) <= 1000:
            expr.append(expressao)
            pergNovamente = False
        else:
            print('Expressão inválida!')

for i in range(0, len(expr)):
    checarparenteses(expr[i])