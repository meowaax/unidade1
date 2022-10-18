cor = str(input('Digite a cor presente no CD: ')).strip().upper()
lista = ['VERDE', 'AZUL', 'AMARELO', 'VERMELHO']
cor.replace(' ', '')
while cor not in lista:
    print('Valor inválido. Por favor digite novamente.')
    cor = str(input('Digite a cor presente no CD: ')).strip().upper()
if 'VERDE' in cor:
    print('O valor do CD é R$10,00')
elif 'AZUL' in cor:
    print('O valor do CD é R$20,00')
elif 'AMARELO' in cor:
    print('O valor do CD é R$30,00')
elif 'VERMELHO' in cor:
    print('O valor do CD é R$40,00')
