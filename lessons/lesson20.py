def lesson20():
    two_digit_number = input("Enter a two-digit number: ")
    if len(two_digit_number) < 2:
        print("You must enter a two-digit number.")
        return
    elif len(two_digit_number) > 2:
        two_digit_number = two_digit_number[:2]

    first_digit = two_digit_number[0]
    second_digit = two_digit_number[1]
    result = int(first_digit) + int(second_digit)
    print(result)
