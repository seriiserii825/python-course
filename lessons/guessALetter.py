import random
def guessALetter():
    words = ['new', 'next', 'second']; 
    choose_word = random.choice(words);
    print(choose_word)

    display = []
    choose_word_length = len(choose_word);
    for _ in range(0, choose_word_length):
        display.append("_")

    end_of_game = False
    attempts = 0;
    while not end_of_game:
        attempts += 1
        print(f'end_of_game: {end_of_game}')
        guess = input('Choose a letter: ').lower()

        for i, letter in enumerate(choose_word):
            if letter == guess:
                display[i] = letter
            else:
                continue

        print(f'display: {display}')
        has_underscore = "_" in display
        print(f'has_underscore: {has_underscore}')
        if not "_" in display:
            end_of_game = True
            print('Your won')
        print(f'attempts: {attempts}')

guessALetter()
