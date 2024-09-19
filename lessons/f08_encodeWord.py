from rich import print
from rich.console import Console
console = Console()
def f08_encodeWord():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    direction = console.input("Type [green]'encode'[/], or [blue]'decode'[/]:") 
    text =console.input('Type your [yellow]message[/]:\n').lower()
    shift = int(console.input("Type the [blue]shif[/] number:\n"))
    caesar(text=text, shift_amount=shift, alphabet=alphabet, direction=direction)

def caesar(text, shift_amount, alphabet, direction):
    final_text = "" 
    alphabet_length = len(alphabet)
    for letter in text:
        position = alphabet.index(letter)
        if (direction == 'encode'):
            if position + shift_amount >= alphabet_length:
                new_position = position + shift_amount - alphabet_length
            else:
                new_position = position + shift_amount
        else:
            if position - shift_amount < 0:
                new_position = alphabet_length + (position - shift_amount)
            else:
                new_position = position - shift_amount
        new_letter = alphabet[new_position]
        final_text += new_letter
    print(f"The [blue]{direction}d[/] text is [green]{final_text}[/]")

f08_encodeWord()
