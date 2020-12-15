print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')

q1 = input(
    "You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")

if q1.lower() == 'left':
    q2 = input('You come to a lake. There is an island in theh middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
    if q2.lower() == 'wait':
        q3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ')
        if q3.lower() == 'blue':
            print('You enter a room of beasts. Game Over.')
        elif q3.lower() == 'yellow':
            print('You Win! You found the treasure')
        elif q3.lower() == 'red':
            print('Its room full of fire. Game Over.')
    else:
        print('Game Over')
else:
    print('Game Over')
