from random import choice
from art import logo, vs
from game_data import data
from os import system
choice1 = choice(data)
choice2 = choice(data)
score = 0
game_over = False
system('clear')
while not game_over:
    while choice1 == choice2:
        choice2 = choice(data)
    choice1_num = choice1['follower_count']
    choice2_num = choice2['follower_count']
    print(logo)
    if score != 0:
        print(f'You\'re right! Current score: {score}.')
    print(
        f'Compare A: {choice1["name"]}, a {choice1["description"]}, from {choice1["country"]}.')
    print(vs)
    print(
        f'Against B: {choice2["name"]}, a {choice2["description"]}, from {choice2["country"]}.')
    guess = input('Who has more followers? Type \'A\' or \'B\': ').lower()
    if guess == 'a':
        statement = choice1_num > choice2_num
    elif guess == 'b':
        statement = choice1_num < choice2_num
    if statement:
        score += 1
    else:
        game_over = True
    system('clear')
    choice1 = choice2
    choice2 = choice(data)
print(logo)
print(f'Sorry, that\'s wrong. Final score: {score}')
