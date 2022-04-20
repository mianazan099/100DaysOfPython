from random import randint
from art import rock, paper, scissors

# Write your code below this line 👇

art = [rock, paper, scissors]

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3:
    print('You typed an invalid number, you lose!')
else:
    print(art[user_choice])
    print('Computer chose:')
    computer_choice = randint(0, 2)
    print(art[computer_choice])

    if user_choice == computer_choice:
        print('It\'s a draw')
    elif user_choice == 2 and computer_choice == 0:
        print('You lose')
    elif user_choice == 0 and computer_choice == 2:
        print('You win!')
    elif user_choice > computer_choice:
        print('You win!')
    elif user_choice < computer_choice:
        print('you lose')
