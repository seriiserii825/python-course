import random
def randomPay():
# You are going to write a program which will
# select arandom name from a list of names. The
# person selected will have to pay for everybody's
# food bill.

# Important: You are not allowed to use the
# choice() function.
# Line 8 splits the string names_string into
# individual names and puts them inside a List
# called names . For this to work, you must enter
# all the names as name followed by comma then
# space. e.g. name, hame, name

    names_string = input("Give me everybody's names, separated by a comma and space. ")
    names = names_string.split(', ')
    names_length = len(names) - 1
    random_index = random.randint(0, names_length)
    print(f"random_index: {random_index}")
    print(f"Name: {names[random_index]}")
