MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(ingredient):
    for item in ingredient:
        if ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    ''' returns the total calculated from coins inserted '''
    total = 0.00
    print('Please insert coins.')
    quarters = int(input('How many quarters?: '))
    total += quarters * 0.25
    print(f'Money inserted: ${total}')
    dimes = int(input('How many dimes?: '))
    total += dimes * 0.10
    print(f'Money inserted: ${total}')
    nickles = int(input('How many nickles?: '))
    total += nickles * 0.05
    print(f'Money inserted: ${total}')
    pennies = int(input('How many pennies?: '))
    total += pennies * 0.01
    print(f'Money inserted: ${total}')
    # total = (quarters * 0.25) + (dimes * 0.10) + \
    #     (nickles * 0.05) + (pennies * 0.01)
    return total


def is_transaction_successful(received, cost):
    ''' return true when the payment is accepted or false if money isn't enough'''
    if received >= cost:
        global profit
        profit += cost
        change = round(received - cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print('Sorry thats not enough money. Money Refunded.')
        return False


def make_coffee(drink, order_ingredients):
    ''' deduct the required ingredients from resources'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your drink {drink}.')


profit = 0
is_on = True
while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ')

    if choice == 'off':
        is_on = False

    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[choice]
        print(f"{choice} will cost you ${drink['cost']}")
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
