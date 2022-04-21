from time import sleep
from lucky_number import lucky_number_game

def game_selector():
    print('############')
    print(' Bem-vindo! ')
    print('############')
    sleep(0.5)

    print('\n')

    print('Escolha o jogo!')
    sleep(0.5)

    print('\n')

    print('[1] Número da Sorte \n[2] Jogo da Forca')
    user_input = int(input(':'))
    sleep(0.5)

    if(user_input == 1):
        lucky_number_game()
    elif(user_input == 2):
        print('Em desenvolvimento!')
    else:
        print('Jogo inválido!')
        return game_selector()