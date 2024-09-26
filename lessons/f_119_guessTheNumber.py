#!/usr/bin/env python3
# Welcome to the Number Guessing Game!
# I'm thinking of a number between 1 and 100.
# Choose a difficulty. Type 'easy' or 'hard': easy
# You have 1@ attempts remaining to guess the number.
# Make a guess: 50
# Too high.
# Guess again.
# You have 9 attempts
# Make a guess: 25
# Too high.
# Guess again.
# You have 8 attempts
# Make a guess: 10
# Too low.
# Guess again.
# You have 7 attempts
# Make a guess: 15
# Too high.
# Guess again.
# You have 6 attempts
# Make a guess: 12
# remaining to guess the number.
# remaining to guess the number.
# &
# remaining to guess the number.
# remaining to guess the number.
# This repl has exited, ?
from random import randint
from replit import clear

from rich import print
from rich.console import Console

def f_119_guessTheNumber():
    clear()
    console = Console()
    answer = intro() 
    attempts = chooseDifficulty()

    while True:
        print(f"You have [blue]{attempts}[/] attempts")
        guess = guessNumber()
        attempts = compare(guess, answer, attempts)
        if attempts == 0:
            print("[red]You limit attempts")
            break
        elif attempts == 'win':
            print("[green]You win")
            break

    try_again = console.input("[green]Do you want to try again? y/n: ")
    if try_again == 'y':
        f_119_guessTheNumber()
    else:
        exit()


def intro():
    print("[green]Welcome to the Number Guessing Game!")
    print("[blue]I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    # print(f"[red] Pssss, answer is {answer}")
    return answer

def chooseDifficulty():
    console = Console()
    print("Choose a difficulty. Type '[green]easy[/]' or '[blue]hard[/]': ")
    difficulty = console.input("")
    if difficulty == 'easy':
        return 10
    else:
        return 5

def guessNumber():
    return int(input("Make a guess: "))

def compare(guess, answer, attempts):
    attempts = attempts - 1
    if guess > answer:
        print("[yellow]Too hight")
        return attempts
    elif guess < answer: 
        print("[blue]Too low")
        return attempts
    elif guess == answer:
        return 'win'

f_119_guessTheNumber()
