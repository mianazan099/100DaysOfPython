from random import randint
from art import logo

print(logo)
print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a number between 1 and 100.')

number = randint(1, 100)
game_over = False

level = input('Choose a difficulty. Type \'easy\' or \'hard\': ').lower()
if level == 'easy':
    lives = 10
else:
    lives = 5

while not game_over:
    print(f'You have {lives} attempts remaining to guess the number.')
    guess = int(input('Make a guess: '))
    if guess == number:
        game_over = True
        print(f'You got it! The answer was {number}.')
    else:
        if guess < number:
            print('Too low.')
        elif guess > number:
            print('Too high.')
        lives -= 1
        if lives == 0:
            game_over = True
            print('You\'ve run out of guesses, you lose.')
        else:
            print('Guess again.')
