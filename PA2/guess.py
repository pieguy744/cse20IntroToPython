# assignment: programming assignment 2
# author: Michael Coe
# date: 10/19/2020
# file: guess.py is an interactive game that asks the user to guess a number from 1 to 10
# input: only integers from 1 to 10
# output: interactive messages

from random import randint

done = False  # initialize the while loop flag
print("Play a game: Guess My Number")

while not done:
    mynumber = randint(1, 10)  # get a random number from 1 to 10
    # put your code here including a for loop
    print('You have three attempts to guess my number.')
    for i in range(3):
        if i == 0:
            print('Please enter a number from 1 to 10:')  # For first attempt
        else:
            print('Guess again. Please enter a number:')

        inp = int(input())
        if inp == mynumber:
            print(f'You guessed right. My number is {mynumber}. Congratulations you won!')  # if guess is correct
            break
        elif inp > mynumber:
            print('You guessed wrong. Your number is bigger than mine.')  # if guess is higher than actual
        else:
            print('You guessed wrong. Your number is smaller than mine.')  # if guess is lower than actual
        if i == 2:
            print(f'Sorry, you lost. My number is {mynumber}.')
    replay = input('Would you like to play again [Y/N]?\n')
    if replay == 'N' or replay == 'n':
        done = True
print("Goodbye!")
