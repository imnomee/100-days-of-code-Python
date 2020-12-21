# Dictionaries
# Key Value Pairs - Objects

programming_dictionary = {
    'Bug': 'An error in a program that prevents the program from running',
    'Function': 'A piece of code that you can easily call over and over again'
}

# Retrieving items
print(programming_dictionary['Bug'])


# Adding items
programming_dictionary['Loop'] = 'The action of doing something over and over again.'
print(programming_dictionary)

# empty dict
empty_dict = {}

# wipe an existing dict
# programming_dictionary = {}


# Edit an item - if key doesn't exist it will create new item
programming_dictionary['Bug'] = 'A moth in your computer.'
print(programming_dictionary)

# Loop through a dict
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#########################################
# Nesting inside dictionary
capitals = {
    'France': 'Paris',
    'Germany': 'Berlin'
}

# Nesting a list inside dict
travel_log = {
    'France': ['Paris', 'Lille', 'Dijon'],
    'Germany': ['Berlin', 'Hamburg', 'Stuttgart'],
}

# Nesting dict in dict
travel_log_dict = {
    'France': {
        'cities_visited': ['Paris', 'Lille', 'Dijon'],
        'total_visits': 12
    },
    'Germany': {
        'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
        'total_visits': 5
    }
}

# Nesting dict inside a list
travel_log_list = [
    {'country': 'France',
     'cities_visited': ['Paris', 'Lille', 'Dijon'],
     'total_visits': 12},
    {'country': 'Germany',
     'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
     'total_visits': 5}
]

print(travel_log_list)
