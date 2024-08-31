def lesson009():
    print("Day 1 - String Manipulation")
    print("String Concatenation is done with the \"+\" sign.")
    print('e.g. print("Hello "' + ' + ' + '"world")')
    result = sum_two_numbers(1, 2)
    print(result)
    new_result = result * 2
    print(f"New result is {new_result}")
    print("New lines can be created with a backslash and n.")

def sum_two_numbers(num1, num2):
    num3 = num1 + num2
    return num3

lesson009()

