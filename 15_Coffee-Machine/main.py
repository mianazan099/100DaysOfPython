MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0
is_on = True


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
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${profit}')
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        drink = MENU[choice]
        if sufficient_resources(drink['ingredients']):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(drink['ingredients'], choice)
