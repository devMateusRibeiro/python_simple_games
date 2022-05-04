from time import sleep
import lucky_number
import hangman

def game_selector():
    print('############\n')
    print(' GAME  MENU \n')
    print('############')
    sleep(0.5)

    print('\n')

    print('Escolha o jogo!')
    sleep(0.5)

    print('\n')

    print('[1] Número da Sorte\n[2] Jogo da Forca')
    user_input = int(input(':'))
    sleep(0.5)

    if(user_input == 1):
        lucky_number.play()
    elif(user_input == 2):
        hangman.play()
    else:
        print('Jogo inválido!')
        return game_selector()

if(__name__ == '__main__'):
    game_selector()