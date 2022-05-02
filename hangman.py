from random import choice

#Retorna uma palavra aleatória dentro de uma lista
def word_choicer():
    wordlist = ['BANANA', 'MAÇA', 'MERCADO', 'FRUTEIRA', 'COMPUTADOR', 'TELEFONE']
    return choice(wordlist)

# Cria uma lista "_" com base no tamanho da palavra passada
def list_maker(word):
    list(word)
    new_list = []

    for x in range(len(word)):
        new_list.append('_')
    return new_list

# Varre a lista procurando por "_", caso não encontrado, retorna True
def list_check(game_list):
    counter = 0
    for x in game_list:
        if x == "_":
            counter += 1
    if counter > 0:
        return False
    else:
        return True

#Desenha o boneco conforme a quantidade de vidas restantes
def drawn_boy(life):
    if(life <= 0):
        print('      O      ')
        print('     /I\     ')
        print('     / \     ')
        print('             ')
    elif(life == 1):
        print('      O      ')
        print('     /I\     ')
        print('     /       ')
        print('             ')
    elif(life == 2):
        print('      O      ')
        print('     /I\     ')
        print('             ')
        print('             ')
    elif(life == 3):
        print('      O      ')
        print('     /I      ')
        print('             ')
        print('             ')
    elif(life == 4):
        print('      O      ')
        print('      I      ')
        print('             ')
        print('             ')
    elif(life == 5):
        print('      O      ')
        print('             ')
        print('             ')
        print('             ')
    elif(life == 6):
        print('             ')
        print('             ')
        print('             ')
        print('             ')

# Função do Jogo da Forca
def play():
    print('Jogo da Forca!')

    word = word_choicer()
    game_word = list_maker(word)

    game_win = False
    lifes = 6
    while(game_win == False and lifes > 0):

        print('_____________')
        print('      |      ')
        print('      |      ')
        drawn_boy(lifes)
        print(game_word)

        letter_input = input('Digite uma letra: ').upper()

        counter = 0
        letter_points = 0
        for x in word:
            if(game_word[counter] == '_' and x == letter_input or game_word[counter] == letter_input):
                game_word[counter] = letter_input
                letter_points += 1
            
            counter += 1

        if(letter_points > 0):
            print(f'A letra "{letter_input}" se encontra nesta palavra!')
            print(f'Vidas restantes: {lifes}')
        else:
            print(f'Você perdeu 1 vida!')
            lifes -= 1
            print(f'Vidas restantes: {lifes}')
        
        if(lifes == 0):
            print('_____________')
            print('      |      ')
            print('      |      ')
            drawn_boy(lifes)
            print(f'A palavra era: {word}')
            print('FIM DE JOGO!')

        game_win = list_check(game_word)

        if(game_win == True):
            print('Parabéns, você ganhou!')
            print(f'A palavra era: {word}')

if(__name__ == '__main__'):
    play()