from random import randint
print('\033[33m-='*40)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[33m-='*40)
print('\033[35mProcessando...\033[m')
cont = 0
valor_aleatorio = randint(0, 5)
acertou = True
while acertou == True:
    chute = int(input('Em que número eu pensei? entre 0 e 5: '))
    if chute != valor_aleatorio:
        print('Voce errou, tente novamente!')
        cont +=1
    if chute == valor_aleatorio:
        print('\033[31mVoce acertou, parabéns!!!')
        cont +=1
        print(f'Voce conseguiu acertar em {cont} tentativas!')
        deseja = str(input('Deseja jogar novamente? [S/N]')).strip()
        if deseja in 'Ss':
             cont = cont - cont
             print('Interessante... vamos para mais uma rodada!')
             valor_aleatorio = randint(0, 5)
        if deseja in 'Nn':
            print('Obrigado por jogar!')
            acertou == False
            break
