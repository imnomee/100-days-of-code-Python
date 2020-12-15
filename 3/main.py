# height in cm
height = int(input('Whats your height in cm?\n'))
bill = 0
age = int(input('Whats your age?\n'))
# > Greater Than
# < Less Than
# <= Less than equal
# >= Greater than equal
# == equal yo
# != not equal
# True or False


if height >= 120:
    print('You can ride the rollercoaster!')
    if age < 12:
        bill = 5
        print(f'Child tickets are ${bill}.')
    elif age <= 18:
        bill = 7
        print(f'Youth tickets are ${bill}.')
    elif age >= 45 and age <= 55:
        print(f'Everything is going to be ok. Have a free ride on us!')
    else:
        bill = 12
        print(f'Adult tickets are ${bill}. ')

    wants_photo = input('Do you want a photo taken? Y or No.\n')
    if wants_photo == 'Y'.lower():
        # Add $3 to their bill
        bill += 3
    print(f'Please pay ${bill}')
else:
    print("Oops! You can't ride today.")
