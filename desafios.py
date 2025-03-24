## minhas repostas para os desafios propostos no curso de python do Curso em vídeo (guanabara)

# DESAFIO 16 (mostra a parte inteira de um numero real)
import math
ìnicio = str(input('deseja iniciar o programa?(sim/nao)'))
while ìnicio == 'sim':
    num = float(input('digite um numero real'))
    print(math.trunc(num))
    break
print('fim do programa.')

# DESAFIO 17 (calcula a hipotenusa de um triangulo retangulo)
import math
cateto1, cateto2 = input('digite os valores dos catetos separados por vírgula').split(',')
cateto1 = float(cateto1)
cateto2 = float(cateto2)
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
print(f'a hipotenusa do trinagulo com catetos {cateto1} e {cateto2} é {hipotenusa}')

# DESAFIO 18 (mostra sen,cos e tag de um angulo qualquer)
import math
angulo = float(input('digite o valor do angulo em graus'))
rad = math.radians(angulo)

sen = math.asin(rad)
cos = math.acos(rad)
tg = math.atan(rad)
print(f'o seno, o coseno e a tangente de {angulo} sao {sen},{cos} e {tg}. respectivamente.')

# DESAFIO 19 (um professor quer escolher um dos quatro alunos aleatoriamente)
import random
a1, a2, a3, a4 = str(input('insira o nome dos alunos separados por virgula')).split(',')

alunos = [a1, a2, a3, a4]
quadro = random.choice(alunos)
print(f'o aluno selecionado foi {quadro}')

# DESAFIO 20 (um professor quer sortar a ordem de apresentaçao dos alunos)
import random
a1 = str(input('insira o nome dos alunos separados por virgula')).split(',')
print('os alunos são:', a1)
sorteio = str(input('dedseja sortear os alunos?'))
while sorteio == 'sim':
    random.shuffle(a1)
    print('a ordem sorteada foi:', a1)
    break
print('fim do programa')

# DESAFIO 22 (crie um programa que leia o nome completo de uma pessoa e mostra:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas.
# Quantos letras do todo (sam considerar espaços).
# Quantas letras tem o primairo nome.)
n = str(input('insira seu nome'))
print(n.upper())
print(n.lower())
print(len(n.replace(' ','')))
print(n.find(' '))

# DESAFIO 23 (crie um programa que leia um numero entre 0 e 9999 e mostre caracter por caracter)
## método 1
n = int(input('insira um numero inteiro(0-9999)'))
num = str(n)
if 0 <= n <= 9:
    unidade = num
    dezena = centena = milhar = '0'
elif 10 <= n <= 99:
    unidade = num[1]
    dezena = num[0]
    centena = milhar = '0'
elif 100 <= n <= 999:
    unidade = num[2]
    dezena = num[1]
    centena = num[0]
    milhar = '0'
elif 1000 <= n <= 9999:
    unidade = num[3]
    dezena = num[2]
    centena = num[1]
    milhar = num[0]
print(f'a unidade é {unidade}, a dezena é {dezena}, a centena é {centena} e o milhar é {milhar}')

## método 2
n = int(input('insira um numero inteiro'))
unidade = n % 10
dezena = (n % 100) // 10
centena = (n % 1000) // 100
milhar = (n % 10000) // 1000
print(f"Unidade: {unidade}, Dezena: {dezena}, Centena: {centena}, Milhar: {milhar}")

# DESAFIO 24 (crie um porgrama que leia o nome de uma cidade e mostre se ele começa com SANTO)
city = str(input('insira o nome da cidade'))
if 'santo' in city[0:6] or 'Santo' in city[0:6]:
    print(' o nome da cidade começa com ''santo'' ')
else:
    print('o nome da cidade nao começa com ''santo'' ')

# DESAFIO 25 (crie um programa que diz se a pessoa tem ou nao ''Santos'' no nome)
nome = str(input('insira o seu nome completo'))
if nome.find('Santos') != -1 or nome.find('santos') != -1:
    print('o ususario possui ''santos'' no nome ')
else:
    print('o usuario nao possui ''santos'' no nome')

# DESAFIO 26 (detectar quantas vezes a letra A aparece em uma frase e qual a primeira e a ultima posiçao)
frase = str(input('Insira uma frase: ')).upper()
contagem = frase.count('A')  
loc = frase.find('A')
lastloc = frase.rfind('A')
print(f"A letra 'A' aparece {contagem} vezes. Primeira ocorrência: posição {loc}. Última ocorrência: posição {lastloc}.")

# DESAFIO 27 (faça um programa que leia um nome completo e mostre o primeiro e o ultimo nome)
nome = str(input('Insira o seu nome completo')).split()
n = nome[0]
nome.reverse()
rl = nome[0]
print(f'seu primeiro nome é {n}. e o seu ultimo nome é {rl}')

# DESAFIO 28
import random 
n = random.randint(1,5)
pergunta = input(‘advinhe o número de 1 a 5’)
if pergunta == n:
    print('parabéns, resposta certa!')
else:
    print('resposta errada')

# DESAFIO 29
v = float(input('insira a velocidade do veiculo'))
multa = (v - 80) * 7
if v > 80:
    print(f'voce pagara uma multa de {multa}')
else:
    print('vcoe nao recebera multa')

# DESAFIO 30
n = int(input('insira um numero inteiro'))
if n % 2 == 0:
    print('o numero escolhido é par')
else: 
    print('numero impar')

# DESAFIO 31
dis = float(input('insira a distancia da viagem em km'))
if dis <= 200:
    taxa = dis * 0.50
    print(f'voce pagará uma taxa de {taxa}')
else:
    taxa = dis * 0.45
    print(f'voce pagará uma taxa de {taxa}')

# DESAFIO 32
ano = int(input('insira o ano'))

if ano % 4 == 0:
    print('ano bissexto')
else: 
    print('o ano nao é bissexto')

# DESAFIO 33
num_list = list(map(int, input('insira tres numeros divididos por espaço: ').split(' ')))
num_list.sort()
print(num_list)
print(f'o menor valor é {num_list[0]}, o maior é {num_list[2]}')
