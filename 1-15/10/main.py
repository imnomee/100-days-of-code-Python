def format_name(f_name, l_name):
    if f_name == '' or l_name == '':
        return "You didn't provide valid inputs."
    full_name = f_name + ' ' + l_name
    if type(f_name) == type(''):
        print('Say hello')
    return full_name.title()


print(format_name('nauman', 'rafiq'))

print(type(1.0))
print(type('s'))
