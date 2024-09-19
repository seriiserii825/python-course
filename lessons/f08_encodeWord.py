def f08_encodeWord():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    direction = input("Type 'encode', or 'decode':") 
    text = input('Type your message:\n').lower()
    shift = int(input("Type the shif number:\n"))

    if direction == 'encode':
        encrypt(plain_text=text, shift_amount=shift, alphabet=alphabet)
    else:
        decrypt(cipher_text=text, shift_amount=shift, alphabet=alphabet)

def encrypt(plain_text, shift_amount, alphabet):
    cipher_text = "" 
    alphabet_length = len(alphabet)
    for letter in plain_text:
        position = alphabet.index(letter)
        if position + shift_amount >= alphabet_length:
            new_position = position + shift_amount - alphabet_length
        else:
            new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount, alphabet):
    plain_text = "" 
    alphabet_length = len(alphabet)
    for letter in cipher_text:
        position = alphabet.index(letter)
        if position - shift_amount < 0:
            new_position = alphabet_length + (position - shift_amount)
        else:
            new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"The encoded text is {plain_text}")


f08_encodeWord()
