import random

user_response = int(input(
    'What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors.'))
print(f"You chose: {user_response}")
computer_response = random.randint(0, 2)
print(f"Computer chose: {computer_response}")


if user_response >= 3 or user_response < 0:
    print('Invalid number. You lose')
elif user_response == 0 and computer_response == 2:
    print('You Win!')
elif user_response == 2 and computer_response == 0:
    print('You lose')
elif computer_response > user_response:
    print('You Lose')
elif user_response > computer_response:
    print('You win!')
elif computer_response == user_response:
    print('Its a draw')
