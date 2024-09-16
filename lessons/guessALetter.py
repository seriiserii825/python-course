import random
def guessALetter():
    words = ['new', 'next', 'second']; 
    choose_word = random.choice(words);
    print(choose_word)

    empty_array = []

    choose_word_length = len(choose_word);
    for _ in range(0, choose_word_length):
        empty_array.append("_")
    # print(empty_array)

    guess = input('Choose a letter: ').lower()
    # print(guess)

    for i, letter in enumerate(choose_word):
        # print(i)
        if letter == guess:
            empty_array[i] = letter
        else:
            continue

    print(empty_array)


guessALetter()
