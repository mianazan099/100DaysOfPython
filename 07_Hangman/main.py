from random import choice
from wordlist import word_list
from art import logo, stages
from os import system
lives = 6
word_array = []
chosen_word = choice(word_list)
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
