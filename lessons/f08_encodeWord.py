import math
def f08_encodeWord():
    test_w  = int(input('Width: '))
    test_h  = int(input('Height: '))
    coverage = 5
    paintCalc(test_w,test_h,coverage)


def paintCalc(width, height, can = 5):
    square = width * height;
    result = math.ceil(square/can)
    print(f"You'l need {result} cans of paint")


f08_encodeWord()
