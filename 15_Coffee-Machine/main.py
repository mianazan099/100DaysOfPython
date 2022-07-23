from data import MENU, resources

profit = 0
is_on = True


def print_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${profit}')


def sufficient_resources(ingredients):
    for key in ingredients:
        if ingredients[key] > resources[key]:
            print(f'Sorry there is not enough {key}.')
            return False
    return True


def process_coins():
    print('Please insert coins.')
    quarters = float(input('how many quarters?: ')) * 0.25
    dimes = float(input('how many dimes?: ')) * 0.10
    nickles = float(input('how many nickles?: ')) * 0.05
    pennies = float(input('how many pennies?: ')) * 0.01
    return round(quarters + dimes + nickles + pennies, 2)


def transaction_successful(money, drink_cost):
    if money >= drink_cost:
        print(f'Here is ${round(money - drink_cost, 2)} dollars in change.')
        global profit
        profit += drink_cost
        return True
    elif money < drink_cost:
        print('Sorry that\'s not enough money. Money refunded.')
        return False


def make_coffee(ingredients, drink):
    global resources
    for key in ingredients:
        resources[key] -= ingredients[key]
    print(f'Here is your {drink} ☕️. Enjoy!')


while is_on:
    choice = input(
        ' What would you like? (espresso/latte/cappuccino): ').lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print_report()
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        drink = MENU[choice]
        if sufficient_resources(drink['ingredients']):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(drink['ingredients'], choice)
