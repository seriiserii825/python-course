def fizzBuzz():
    for i in range(1, 101):
        divide_to_3 = i % 3 == 0
        divide_to_5 = i % 5 == 0
        if divide_to_3 and divide_to_5:
            print('FizzBuzz')
        elif divide_to_3:
            print('Fizz')
        elif divide_to_5:
            print('Buzz')
        else:
            print(i)
fizzBuzz()
