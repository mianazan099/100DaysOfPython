from os import system
from random import choice
from art import logo, stages
from wordlist import word_list

chosen_word = choice(word_list)
lives = 6

word_array = []
for _ in chosen_word:
    word_array.append('_')

print(logo)

while lives > 0 and '_' in word_array:
    guess = input('Guess a letter: ').lower()
    system('clear')

    if guess in word_array:
        print(f'You\'ve already guessed {guess}')

    if guess in chosen_word:
        for n in range(len(chosen_word)):
            if chosen_word[n] == guess:
                word_array[n] = chosen_word[n]
        print(' '.join(word_array))
        if '_' not in word_array:
            print('You Win')

    else:
        print(' '.join(word_array))
        print(
            f'You guessed {guess}, that\'s not in the word. You lose a life.')
        lives -= 1
        if lives == 0:
            print('You lose')

    print(stages[lives])
