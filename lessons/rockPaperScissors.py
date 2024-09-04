import random
from rich import print
from rich.console import Console
console = Console()

def rockPaperScissors():
    # « Rock wins against scissors.
# « Scissors win against paper.
# « Paper wins against rock.
    str_choices = ['Rock', 'Scissors', 'Paper']
    all_choice = [0, 1, 2]
    computer_choice = random.choice(all_choice)
    choose = int(console.input("What do you choose? Type [green]0[/] for Rock, [blue]1[/] for Paper or [yellow]2[/] for Scissors."))

    print(f"[blue]Computer choice: {str_choices[computer_choice]}")
    print(f"[yellow]Your choice: {str_choices[choose]}")
    lost = '[red]Your lost'
    win = '[green]Your win'
    if computer_choice == 0 and choose == 1:
        print(lost)
    elif(computer_choice == 1 and choose == 2):
        print(lost)
    elif(computer_choice == 2 and choose == 0):
        print(lost)
    elif(computer_choice == choose):
        print(f'[blue]Equal')
    else:
        print(win)

