#!/usr/bin/env python3
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10. 1
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

#Difficulty Normal @: Use all Hints below to complete the project.
#Difficulty Hard @: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard @: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert @: Only use Hint 1 to complete the project. 56

#Hint 1: Go to this website and try out the Blackjack game:
# https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
# https://blackjack-final.appbrewery.repl.run 1
#Hint 2: Read this breakdown of program requirements:
# http://listmoz.com/view/6h34DIpvIBFVR1ZfIVXF
#Then try to create your own flowchart for the program.
#Hint 3: Download and read this flow chart I've created:
#  https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjMlqwSuyEk-rPnt
#Hint 4: Create a deal_card() function that uses the List below to *returnx a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random
from rich import print
from rich.panel import Panel
from replit import clear
def f_108_blackJack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    is_game_over = False
    print(f"cards: [green]{cards}")
    user_cards = []
    computers_cards = []
    user_score = 0
    computers_score = 0
    user_cards = getRandomCards(2, cards)
    computers_cards = getRandomCards(2, cards)

    while not is_game_over:
        user_score = calculateScore(user_cards)
        computers_score = calculateScore(computers_cards)
        print(Panel(f"User cards: [green]{user_cards}[/], score: [blue]{user_score}[/]"))
        print(Panel(f"Computers first card: [yellow]{computers_cards[0]}"))

        if user_score == 0 or computers_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to end the game: ")
            if user_should_deal == 'y':
                user_cards.append(dealCard(cards))
            else:
                is_game_over = True
    
    while computers_score != 0 and computers_score < 17:
        computers_cards.append(dealCard(cards))
        computers_score = calculateScore(computers_cards)

    print(Panel(f" Your finel hand: [green]{user_cards}[/], final_score: [blue]{user_score}[/]"))
    print(Panel(f" Computers finel hand: [green]{computers_cards}[/], final_score: [blue]{computers_score}[/]"))
    print(compare(user_score=user_score, computers_score=computers_score))

    play_again = input('Do you want to play again? Type "y" or "n": ')
    if play_again == 'y':
        clear()
        f_108_blackJack()
    else:
        print('[red]Goodbye')
        exit()

def getRandomCards(count, cards):
    """Return a random 'count' cards as array"""
    total_cards = []
    for _ in range(count):
        total_cards.append(dealCard(cards))
    return total_cards


def dealCard(cards):
    """Return random card from cards"""
    return random.choice(cards)

def calculateScore(cards):
    """Take a list  of cards and calculate score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computers_score):
    if user_score == computers_score:
        return "[blue]Draw"
    elif computers_score == 0:
        return '[red]Your loose, opponent has BlackJack'
    elif user_score == 0:
        return '[green]Win with a BlackJack'
    elif user_score > 21:
        return '[red]You went over, lose'
    elif computers_score > 21:
        return '[green]Opponnet went over, you win'
    elif computers_score > user_score:
        return '[green]You win'
    else: 
        return '[red]You lose'

f_108_blackJack()

