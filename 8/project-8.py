from cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(direction, text, shift):
    cipher_text = ''
    if direction == 'decode':
        shift = shift * (-1)
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f"The {direction}d text is: {cipher_text}")


should_continue = True
while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25   # incase user enters a larger shift

    caesar(direction, text, shift)
    restart = input(
        f"Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if restart == 'no':
        print('Goodbye')
        should_continue = False

# def decrypt(text, shift):
#     cipher_text = ''
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         cipher_text += alphabet[new_position]
#     print(f"The decoded text is: {cipher_text}")


# def encrypt(text, shift):
#     cipher_text = ''
#     # for i in range(0, len(alphabet)):
#     #     for j in range(0, len(text)):
#     #         if text[j] == alphabet[i]:
#     #             cipher_text += alphabet[i + shift]

#     for letter in text:
#         # index function gives us the first index it found
#         position = alphabet.index(letter)
#         new_position = position + shift
#         cipher_text += alphabet[new_position]
#     print(f"The encoded text is: {cipher_text}")


# if direction == 'encode':
#     encrypt(text, shift)
# elif direction == 'decode':
#     decrypt(text, shift)
# else:
#     print('Invalid Direction')
