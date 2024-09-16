import math
def f08_encodeWord():
    test_w  = int(input('Width: '))
    test_h  = int(input('Height: '))
    coverage = 5
    paintCalc(width=test_w,height=test_h,can=coverage)


def paintCalc(width, height, can = 5):
    square = width * height;
    result = math.ceil(square/can)
    print(f"You'l need {result} cans of paint")


f08_encodeWord()
