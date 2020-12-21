import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# choice function
# name is chosen from the list, we don't need to catch the index first
# random_name = random.choice(names)

random_name = random.randint(0, len(names)-1)
print(f"{names[random_name]} is going to buy the meal today!")
