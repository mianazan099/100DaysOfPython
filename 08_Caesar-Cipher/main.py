from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet += alphabet
cipher_on = True


def encode(text, shift, direction):
    shift %= 26
    final_word = ''
    for n in text:
        if n not in alphabet:
            final_word += n
        else:
            if direction == 'encode':
                final_word += alphabet[alphabet.index(n) + shift]
            else:
                final_word += alphabet[alphabet.index(n) - shift]
    print(f'Here\'s the {direction}d result: {final_word}')


print(logo)
while cipher_on:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == 'decode' or direction == 'encode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encode(text, shift, direction)
        go_again = input(
            'Type \'yes\' if you want to go again. Otherwise type \'no\'.\n').lower()
        if go_again != 'yes':
            print('Goodbye')
            cipher_on = False
    else:
        print('Invalid Choice')
