import random

def main():

    moves = ['rock','paper','scissors']
    print('For this game you have to type one of the three objects. To exit the game enter "exit"')

    while(True):

        score = open('game.txt','w')
        score.write('Number of wins: ')
        user_input = input('Rock, Paper, Scissors? ').lower()
        computer = random.choice(moves)
        wins = 0

        if computer == user_input:
            print('Tie')
            if user_input == 'exit':
                break

        elif computer == 'rock' and user_input == 'scissors':
            print('Rock crushes scissors.')
            if user_input == 'exit':
                break


        elif computer == 'rock' and user_input == 'paper':
            wins += 1
            score.write(str(wins))
            print('Paper covers rock.')
            if user_input == 'exit':
                break



        elif computer == 'paper' and user_input == 'scissors':
            wins += 1
            score.write(str(wins))
            print('Scissors cuts paper.')
            if user_input == 'exit':
                break

        elif computer == 'paper' and user_input == 'rock':
            print('Paper covers rock.')
            if user_input == 'exit':
                break


        elif computer == 'scissors' and user_input == 'paper':
            print('Scissors cuts paper.')
            if user_input == 'exit':
                break


        elif computer == 'scissors' and user_input == 'rock':

            wins += 1
            score.write(str(wins))
            print('Rock crushes scissors.')
            if user_input == 'exit':
                break

        else:
            print('Please choose between rock, paper or scissors!')
            if user_input == 'exit':
                break


main()