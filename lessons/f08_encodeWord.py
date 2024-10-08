from rich import print
from rich.console import Console
console = Console()
def f08_encodeWord():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    direction = console.input("Type [green]'encode'[/], or [blue]'decode'[/]:") 
    text =console.input('Type your [yellow]message[/]:\n').lower()
    shift = int(console.input("Type the [blue]shif[/] number:\n"))
    #when shift is greater than the length of the alphabet get the remainder
    shift = shift % len(alphabet)

    caesar(text=text, shift_amount=shift, alphabet=alphabet, direction=direction)
def caesar(text, shift_amount, alphabet, direction):
    final_text = "" 
    alphabet_length = len(alphabet)
    for letter in text:
        if letter in alphabet:
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
        else:
            final_text += letter
    print(f"The [blue]{direction}d[/] text is [green]{final_text}[/]")
    go_again = console.input("Do you want to [blue]go again[/]? [green]yes[/] or [red]no[/]:")
    if go_again == 'yes':
        f08_encodeWord()
    else:
        console.print("[red]Goodbye!")
        exit()

f08_encodeWord()
