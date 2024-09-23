from replit import clear

from logos.calc_logo import calc_logo
print(calc_logo)

#add
def add(a, b):
    return a + b
#subtract
def subtract(a, b):
    return a - b
#multiply
def multiply(a, b):
    return a * b
#divide
def divide(a, b):
    return a / b
operations = {
        "+": add,
        "-": subtract,
        "/": divide,
        "*": multiply
        }

def f_101_calculator():
    continue_calculation = True
    answer = 0
    first_step = True

    while continue_calculation:
        if first_step:
            num1 = float(input('first number? '))
            first_step = False
        else:
            num1 = answer
        for sign in operations:
            print(sign)
        operation_sign = input("Use a operation sign: ")
        num2 = float(input('second number?: '))
        calculation_function = operations[operation_sign]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_sign} {num2} = {answer}")
        next_step = input('Do you want to continue or start new, type n to new? ')
        if next_step == 'n':
            continue_calculation = False
            clear()
            f_101_calculator()

f_101_calculator()
            
