import random
# random uses the timestamp as a seed to generate random numbers
# we can change the seed by

random.seed(38748378579)
# random int numbers
random_int = random.randint(1, 100)
# print(random_int)

# random float number between 0 and 1.0
random_fl = random.random()

# random float number between 1 and 5
random_float = int(random.random() * 5)+1
# print(random_float)

love_score = random.randint(0, 1)  # 0 and 1 only
# print(love_score)


# LISTS
# ordered data, by entrty
states_of_america = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia',
                     'Connecticut', 'Maryland', 'Virginia', 'New York', 'Rhode Island']

# https://docs.python.org/3/tutorial/datastructures.html
# change item
states_of_america[1] = 'Pensylvania'
# add a single item at the end
states_of_america.append('Nomeeland')

# add multiple items at the end or adding a list at the end
states_of_america.extend(['one', 'two', 'lol'])
# print(states_of_america)

# print(states_of_america[len(states_of_america)-1])
# print(len(states_of_america))

dirty_dozen = ['Strawberries', 'Spinach', 'Kale', 'Nectarines', 'Apples',
               'Grapes', 'Peaches', 'Cherries', 'Pears', 'Tomatoes', 'Celery', 'Potatoes']
