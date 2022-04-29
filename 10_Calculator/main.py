from art import logo
from os import system


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    print(logo)
    num1 = float(input('What\'s the first number?: '))
    print('+\n-\n*\n/')
    continue_calc = 'y'
    while continue_calc == 'y':
        operation = input('Pick an operation: ')
        num2 = float(input('What\'s the next number?: '))
        calculation = operations[f'{operation}'](num1, num2)
        print(f'{num1} {operation} {num2} = {calculation}')
        continue_calc = input(
            f'Type \'y\' to continue calculating with {calculation}, or type \'n\' to start a new calculation: ').lower()
        num1 = calculation
    system('cls' or 'clear')
    calculator()


calculator()

# you can also use: eval()