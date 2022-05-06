# from data import resources, MENU
# money = 0
# game_over = False
# def print_report():
#     print(f'Water: {resources["water"]}ml')
#     print(f'Milk: {resources["milk"]}ml')
#     print(f'Coffee: {resources["coffee"]}g')
#     print(f'Money: ${money}')
# def take_payment():
#     print('Please insert coins.')
#     quarters = float(input('how many quarters?: '))
#     dimes = float(input('how many dimes?: '))
#     nickles = float(input('how many nickles?: '))
#     pennies = float(input('how many pennies?: '))
#     return round(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01, 2)
# def check_transaction(payment, coffee_cost):
#     if payment >= coffee_cost:
#         print(f'Here is ${round(payment - coffee_cost, 2)} dollars in change.')
#         global money
#         money += coffee_cost
#         return True
#     elif payment < coffee_cost:
#         print('Sorry that\'s not enough money. Money refunded.')
#         return False
# def have_resources(order_ingredients):
#     for order in order_ingredients:
#         if order_ingredients[order] > resources[order]:
#             print(f"Sorry there is not enough {order}.")
#             return False
#     return True
# def make_coffee(drink_name, order_ingredients):
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f'Here is your {drink_name} ☕️. Enjoy!')
# while not game_over:
#     user_choice = input(' What would you like? (espresso/latte/cappuccino): ').lower()
#     if user_choice == 'off':
#         game_over = True
#     elif user_choice == 'report':
#         print_report()
#     elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
#         drink = MENU[user_choice]
#         if have_resources(drink['ingredients']):
#             payment = take_payment()
#             if check_transaction(payment, drink['cost']):
#                 make_coffee(user_choice, drink['ingredients'])
