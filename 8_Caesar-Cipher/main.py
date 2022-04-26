from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet += alphabet
go_again = 'yes'


def encode(text, shift, direction):
    shift %= 26
    final_word = ''
    for n in text:
        if n not in alphabet:
            final_word += n
        else:
            if direction == 'encode':
                final_word += alphabet[alphabet.index(n) + shift]
            elif direction == 'decode':
                final_word += alphabet[alphabet.index(n) - shift]
    print(f'Here\'s the {direction}d result: {final_word}')


print(logo)
while go_again == 'yes':
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encode(text, shift, direction)
    go_again = input(
        'Type \'yes\' if you want to go again. Otherwise type \'no\'.\n').lower()
    if go_again == 'no':
        print('Goodbye')
