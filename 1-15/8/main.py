def greet():
    print('Hello')
    print('There')
    print('N.R')


# functions with input
def greet_with_name(name):
    print(f'Hello! {name}')


greet_with_name('nauman')

# multiple input functions


def greet_with(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}')


greet_with('nauman', 'Rawalpindi')

# functions with positional paramenters/ arguments
greet_with(location='Rawalpindi', name='Nauman')
