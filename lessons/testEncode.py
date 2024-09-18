def testEncode():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text = input("Enter a text: ")
    shift = int(input("Enter a shift value, number: "))
    encode(plain_text=text, shift_amount=shift, alphabet=alphabet)


def encode(plain_text, shift_amount, alphabet):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        total_position  = position + shift_amount
        alphabet_len = len(alphabet)
        if total_position > alphabet_len:
            new_position = (total_position) - alphabet_len
        else:
            new_position = total_position
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(cipher_text)

testEncode()
