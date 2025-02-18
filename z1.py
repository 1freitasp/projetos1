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
