## primeiro projeto usando laços de repetiçao
## consiste em um jogo onde o usuario tem que inserir informações iniciais e responder uma pergunta

nome = str(input("olá,qual o seu nome?"))
print("olá", nome)
jogo = str(input("quer jogar um jogo?"))
while jogo == "sim":
    print("ok, vamos lá")
    soma = int(input("quanto é 1 + 3?"))
    if soma == 4:
        print("parabéns, voce acertou!")
        jogo = str(input("quer jogar novamente?"))
    else: 
        print("resposta errada")
        jogo = str(input("quer tentar novamente?"))
print("tudo bem {}. até a proxima!".format(nome))

## atualizaçao do código, dessa vez com mais funcionalidades

nome = str(input('olá! qual o seu nome?'))
pergunta = str(input(f'olá {nome}, posso te fazer uma pergunta?'))
while pergunta == 'sim':
    n1 = int(input('me diga um numero inteiro'))
    n2 = int(input('diga outro'))
    soma = int(input('agora me diga a soma desses dois numeros'))
    if soma == n1 + n2:
        print(f'a soma entre {n1} e {n2} é {n1 + n2}') 
        print('parabens, voce acertou!')
        pergunta = str(input('quer continuar? (sim/nao)'))
    else:
        print('voce errou')
    print(f'a soma entre {n1} e {n2} é {n1 + n2}') 
    pergunta = str(input('quer tentar novamente?'))
print(f'tudo bem {nome}, até a proxima!')
