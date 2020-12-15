# Data Types
# String
print('Hello'[1])

# integar Whole numbers
print(123 + 345)
print(123_345 + 2)

# FLoat - Decimal Points
3.1415

# Booleans
True or False

nameLength = 7

# type checking
print(type(nameLength))

# type conversion
stringType = str(nameLength)
print(type(stringType))

a = 123
print(type(a))
print(type(str(a)))

print(type(3 + 5))
print(type(7 - 4))
print(type(3 * 2))
print(type(6/3))

# Exponent (pow)
print(5**10)

# PEMDAS calculation rules
# Parentheses ()
# Exponents**
# Multiplication *
# Division /
# Addition +
# Subtraction -

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

num = 8/3
print(int(num))
print(round(num))
print(round(num, 2))

# int conversion
print(8 // 3)

score = 0
# user scores a point
score += 3
height = 1.8
isWinning = True
# f-string
print(
    f"Your score is {score}, height is {height} and you are winning: {isWinning}")
