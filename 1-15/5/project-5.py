import random

# Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letters_len = len(letters)
numbers_len = len(numbers)
symbols_len = len(symbols)

initial_pass = ''  # this list cant be shuffled
pass_list = []  # we can shuffle if the passwords are saved in a list

for letter in range(0, nr_letters):
    rand_letter = random.randint(0, letters_len-1)
    initial_pass += letters[rand_letter]
    pass_list.append(letters[rand_letter])
    # print(letters[rand_letter])

print(initial_pass)
for num in range(0, nr_numbers):
    rand_num = random.randint(0, numbers_len - 1)
    initial_pass += numbers[rand_num]
    pass_list.append(numbers[rand_num])

print(initial_pass)

for num in range(0, nr_symbols):
    rand_sym = random.randint(0, symbols_len - 1)
    initial_pass += symbols[rand_sym]
    pass_list.append(symbols[rand_sym])

print(f"Un-random: \t\t\t{initial_pass}")
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# shuffle the password list
final_password = ''
random.shuffle(pass_list)
for chr in pass_list:
    final_password += chr

print(f'Random password: \t{final_password}')
