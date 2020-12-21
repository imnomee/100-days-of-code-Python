import os
import random
from art import logo, vs
from game_data import data


def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


os.system('cls')

print(logo)
score = 0
game_over = False
account_b = random.choice(data)
while not game_over:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    answer = input('Who has more followers? Type "A" or "B": ').lower()

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    is_correct = check_answer(answer, a_followers, b_followers)
    os.system('cls')
    print(logo)
    if is_correct:
        score += 1
        print(f'You are right!: Current score: {score }')
    else:
        game_over = True
        print(f'Sorry, thats wrong. Final Score: {score}')
