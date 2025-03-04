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


