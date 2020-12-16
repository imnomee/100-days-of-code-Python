# Write your code below this row 👇
for num in range(1, 100):
    if num % 5 == 0 and num % 3 == 0:
        print(num)
        print('FizzBuzz')
    elif num % 3 == 0:
        print(num)
        print('Fizz')
    elif num % 5 == 0:
        print(num)
        print('Buzz')
    else:
        print(num)
