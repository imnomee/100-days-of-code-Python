# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random
# test_seed = int(input('Create a seed number: '))
# random.seed(test_seed)

random_number = random.randint(0, 1)
if random_number == 0:
    print('Tails')
else:
    print('Heads')
