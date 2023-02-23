import random

while True:
    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('rock, paper, scissors?: ')
    if player == computer:
        print('Computer: ', computer)
        print('Player: ', player)
        print('Tie!')
    elif player == 'rock':
        if computer == 'paper':
            print('Computer: ', computer)
            print('Player: ', player)
            print('Tie!')
        if computer == 'scissors':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You win!')
    elif player == 'scissors':
        if computer == 'rock':
            print('Computer: ', computer)
            print('Player: ', player)
            print('Tie!')
        if computer == 'paper':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You win!')
    elif player == 'rock':
        if computer == 'paper':
            print('Computer: ', computer)
            print('Player: ', player)
            print('Tie!')
        if computer == 'scissors':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You win!')
    play_again = input('Play again (yes/no):  ')

    if play_again != 'yes':
        break
print('Byeeeeee')
