game_level = 3
enemies = ['Skeleton', 'Zombie', 'Alien']

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)  # valid scope. you can access it in conditions

# if we change the conditional scope to funcitons, it won't access it.


def create_enemy():
    if game_level < 5:
        new_enemy_b = enemies[0]
# print(new_enemy_b)

########################
# CHANGING GLOBAL SCOPE


enemies = 1


def increase_enemies():
    # global enemies  # takes global variable and modifies it
    # enemies += 10
    print(f'enemies inside function: {enemies}')
    return enemies + 10


enemies = increase_enemies()
print(f'enemies outside fuction: {enemies}')

########################
# CONSTANTS
# naming convetion is to change to uppercase

PI = 3.14159


def calc():
    print(pi)
