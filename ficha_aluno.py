from time import sleep
print('INICIANDO...')
sleep(1)
aprov = ' '
nome = str(input('Digite seu nome completo: ').strip().upper())
curso = str(input('Digite seu curso: ')).strip().upper()
p = int(input('Digite o período que está cursando: '))
while 0 >= p > 16:
    print('Valor inválido para período. Por favor, insira um novo valor.')
    p = int(input('Digite o período que está cursando: '))
n1 = float(input('Digite o valor da primeira nota: '))
while 0 > n1 > 10:
    print('Valor inválido para 1º nota. Por favor, insira um novo valor.')
    n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))
while 0 > n2 > 10:
    print('Valor inválido para 2º nota. Por favor, insira um novo valor.')
    n2 = float(input('Digite o valor da segunda nota: '))
faltas = int(input('Digite a quantidade de faltas nesse semestre: '))
while 0 > faltas > 10:
    print('Valor inválido para quantidade de faltas. POr favor, insira um novo valor.')
    faltas = int(input('Digite a quantidade de faltas nesse semestre: '))
media = (n1 + n2)/2
if media >= 7 and faltas <= 3:
    aprov = 'Aluno aprovado'
else:
    aprov = 'Aluno reprovado'
if 'SI' in curso:
    curso = 'Sistemas de Informação'
print('ANALISANDO...')
sleep(2)
print('NOME: {} \n'
      'CURSO: {} \n'
      'PERÍODO: {} \n'
      '1º NOTA: {} \n'
      '2º NOTA: {} \n'
      'NÚMERO DE FALTAS: {} \n'
      'MÉDIA: {} - {} \n'.format(nome, curso, p, n1, n2, faltas, media, aprov))
print('........................ \n'
      'FIM DO PROGRAMA')
