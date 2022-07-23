import random
from os import system
from art import logo


def deal_card(array, num):
    for _ in range(num):
        array.append(random.choice(cards))


def stats():
    print(f'   Your cards: {user_cards}, current score: {sum(user_cards)}')
    print(f'   Computer\'s first card: {computer_cards[0]}')


def check_score():
    user_cards_sum = sum(user_cards)
    computer_cards_sum = sum(computer_cards)

    if user_cards_sum == computer_cards_sum:
        return 'Draw 🙃'
    elif user_cards_sum == 21 and len(user_cards) == 2:
        return 'Win with a Blackjack 😎'
    elif computer_cards_sum == 21 and len(computer_cards) == 2:
        return 'Lose, opponent has Blackjack 😱'
    elif user_cards_sum > 21:
        return 'You went over. You lose 😭'
    elif computer_cards_sum > 21:
        return 'Opponent went over. You win 😁'
    elif user_cards_sum < computer_cards_sum:
        return 'You lose 😤'
    elif user_cards_sum > computer_cards_sum:
        return 'You win 😃'


def blackjack():
    print(logo)
    deal_card(user_cards, 2)
    deal_card(computer_cards, 2)
    stats()

    blackjack_game = True
    while sum(user_cards) < 21 and blackjack_game:
        want_another_card = input(
            'Type \'y\' to get another card, type \'n\' to pass: ').lower()
        if want_another_card == 'y':
            deal_card(user_cards, 1)
            if sum(user_cards) > 21:
                if 11 in user_cards:
                    user_cards.remove(11)
                    user_cards.append(1)
            stats()
        else:
            blackjack_game = False
    while sum(computer_cards) < 17:
        deal_card(computer_cards, 1)
    print(f'   Your final hand: {user_cards}, final score: {sum(user_cards)}')
    print(
        f'   Computer\'s final hand: {computer_cards}, final score: {sum(computer_cards)}')
    print(check_score())


play_game = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = []
user_cards = []

while play_game:
    want_to_play = input(
        'Do you want to play a game of Blackjack? Type \'y\' or \'n\': ').lower()
    if want_to_play == 'y':
        system('cls' or 'clear')
        blackjack()
        user_cards = []
        computer_cards = []
    else:
        play_game = False
