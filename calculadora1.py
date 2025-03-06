## primeiro projeto de calculadora 
n1 = float(input('insira o primeiro valor'))
n2 = float(input('insira um segundo valor'))
operacao = str(input('qual operaçao deseja realizar?'))
if operacao == 'soma':
    print(f'o resultado da soma entre {n1} e {n2} é {n1 + n2}')
elif operacao == 'subtracao':
    print(f'o resultado da subtração entre {n1} e {n2} é {n1 - n2}')
elif operacao == 'multiplicacao':
    print(f'o resultado da multiplicação entre {n1} e {n2} é {n1 * n2}')
elif operacao == 'divisao':
    if n2 != 0:
        print(f'o resultado da divisão entre {n1} e {n2} é {n1 / n2}')
    else:
        print('Erro: divisão por zero não é permitida')
