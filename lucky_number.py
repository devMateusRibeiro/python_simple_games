from random import randrange
from time import sleep

# Função para a seleção de dificuldade do Game
def difficult(difficult_input):
    if(difficult_input == 1):
        return 20
    elif(difficult_input == 2):
        return 10
    elif(difficult_input == 3):
        return 5
    else:
        print('Nível inválido!')
        return lucky_number_game()

# Função do Game
def lucky_number_game():
    print('\nNúmero da Sorte! \n')
    sleep(0.5)

    secret_number = randrange(1, 101)

    counter = 1;

    print('Escolha uma dificuldade: \n[1] Fácil\n[2] Médio\n[3] Difícil')
    sleep(0.5)
    difficult_input = int(input(':'))
    sleep(0.5)

    rounds = difficult(difficult_input)

    while counter <= rounds:
        print(f'Rodada {counter} de {rounds}! \n')
        sleep(0.5)

        user_num = int(input('Escolha um número de 1 a 100:'))
        sleep(0.5)

        if(counter != rounds):
            if(user_num > 0 and user_num < 101):
                if(user_num == secret_number):
                    print(f'A máquina escolheu o número: {secret_number}')
                    print('Parabéns, você acertou o número!')
                    sleep(0.5)
                    break
                else:
                    if(user_num > secret_number):
                        print('Você chutou um número MAIOR que máquina! \n')
                        sleep(0.5)
                        counter += 1
                    else:
                        print('Você chutou um número MENOR que máquina! \n')
                        sleep(0.5)
                        counter += 1    
            else:
                print('Número inválido!\n')
                sleep(0.5)
        else:
            print('Rodadas acabaram!')
            sleep(0.5)
            