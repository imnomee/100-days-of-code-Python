from art import logo
import os


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# symbols
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    os.system('cls')
    print(logo)

    calc_on = True
    num1 = float(input("What's the first number?: "))

    while calc_on:
        for symbol in operations:
            print(symbol)
        operation_symbol = input('Pick an operation: ')
        num2 = float(input("What's the next number?: "))
        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        reset = input(
            f"Type 'y' to continue calculating with {answer} or type 'n' to exit.: ")
        if reset == 'n':
            calc_on = False
            calculator()
        else:
            num1 = answer


calculator()
