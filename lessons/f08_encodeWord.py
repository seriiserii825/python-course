def f08_encodeWord():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # direction = input("Type 'encode', or 'decode':") 
    text = input('Type your message:\n').lower()
    shift = int(input("Type the shif number:\n"))

    encrypt(text, shift, alphabet)

def encrypt(plain_text, shift_amount, alphabet):
    cipher_text = "" 
    for letter in plain_text:
       position = alphabet.index(letter)
       new_position = position + shift_amount
       new_letter = alphabet[new_position]
       cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


f08_encodeWord()
