import os
import random
from art import logo


def check_answer(guess, rand_number, guesses):
    if guess > rand_number:
        print('Too high')
        return guesses - 1
    elif guess < rand_number:
        print('Too low')
        return guesses - 1
    elif guess == rand_number:
        print(f"You got it! The answer was {rand_number}")


def generate_number():
    return random.randint(1, 100)


def game():
    os.system('cls')
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")
    rand_number = generate_number()
    print(rand_number)

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    guesses = 0
    game_finished = False

    if difficulty == 'hard':
        guesses = 5
    elif difficulty == 'easy':
        guesses = 10

    guess = 0
    while guess != rand_number:
        print(f'You have {guesses} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))
        guesses = check_answer(guess, rand_number, guesses)
        if guesses == 0:
            print("You've run out of guesses, you lose")
            return


game()
