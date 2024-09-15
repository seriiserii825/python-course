import random
def guessALetter():
    words = ['new', 'next', 'second']; 
    choose_word = random.choice(words);
    print(choose_word)
    guess = input('Choose a letter: ').lower()
    print(guess)

guessALetter()
