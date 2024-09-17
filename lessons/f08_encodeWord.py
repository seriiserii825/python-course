def f08_encodeWord():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    direction = input("Type 'encode', or 'decode':") 
    print(f'direction: {direction}')
    if direction != 'encode' and direction != 'decode':
        print('wrong choice')
        exit()
    text = input('Type your message:\n').lower()
    shift = int(input("Type the shif number:\n"))
    if text != '' and shift != '':
        if direction == 'encode':
            encrypt(text,shift, alphabet)
    else:
        print('use shift and text')
        exit()



def encrypt(text, shift, alphabet):
    alphabet_len = len(alphabet)
    for index, letter in enumerate(text):
        print(f"index: {index}")
        alphabet_index = getLetterIndex(letter, alphabet)
        print(f"alphabet_index: {alphabet_index}")
        if alphabet_index:
            new_index = alphabet_index + shift
            # print(f"new_index: {new_index}")
            new_letter = alphabet[new_index]
            # print(f"new_letter: {new_letter}")
            text = list(text)
            text[index] = new_letter
            text = "".join(text)
    print(f"text: {text}")

def getLetterIndex(letter, alphabet):
    for index, item in enumerate(alphabet):
        if item == letter:
            return index
    return False

           
# def primeChecker(number):
#     for i in range(2, number):
#         if number % i == 0:
#             print("It's not a prime number")
#             return
#     print("It's a prime number")
#
#
# def paintCalc(width, height, can = 5):
#     square = width * height;
#     result = math.ceil(square/can)
#     print(f"You'l need {result} cans of paint")


f08_encodeWord()
