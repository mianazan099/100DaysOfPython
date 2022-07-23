from os import system
from art import logo

bidders = {}
other_bidders = True


def get_info():
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    bidders[name] = bid


print(logo)
while other_bidders:
    get_info()
    other_bidders = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bidders == 'yes':
        system('clear' or 'cls')
    else:
        other_bidders = False

person = ''
bid = 0
for n in bidders:
    if bidders[n] > bid:
        bid = bidders[n]
        person = n

print(f"The winner is {person} with a bid of ${int(bid)}")
