import random
import hangman_art
import hangman_words

# clear console from the file
# then use clear() frunctoin where required
import os
def clear(): return os.system('cls')


# from hangman_art import logo
# from hangman_art import stages

word_list = hangman_words.word_list
stages = hangman_art.stages
logo = hangman_art.logo

print(logo)
lives = 6
# rand_ind = random.randint(0, len(word_list) - 1)
# chosen_word = word_list[rand_ind]
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for letter in chosen_word:
    display.append('_')

# print(display)
# print(display.count('_'))

# while display.count('_') > 0:
end_of_game = False

while not end_of_game:
    guess = input('Guess a letter: \n')[0].lower()
    clear()
    if guess in display:
        print(f"You have already chosen: {guess}")
    for ind in range(len(chosen_word)):
        if chosen_word[ind] == guess:
            print(stages[lives])
            display[ind] = guess
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        # print(f'Lives Left: {lives}')
        print(stages[lives])
        if lives == 0:
            print('You Lose')
            end_of_game = True

    print(display)

    if '_' not in display:
        print('You Won. Game Over')
        end_of_game = True
