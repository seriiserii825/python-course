def tipCalculator():
    print("Welcome to the tip calculator.")
    total_bill = round(float(input("What was the total bill?$")), 2)
    people_count = int(input("How many people to split the bill? "))
    percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    percent_array = [10, 12, 15]
    if (not percentage in percent_array):
        print("Percentage is wrong")
        exit()
    percent_calc = percentage / 100 + 1
    result = (total_bill / people_count) *  percent_calc
    result = "{:.2f}".format(result)

    print(f"Each person should pay: ${result}")
