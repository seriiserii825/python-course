def lesson020():
    height = input("Enter your height in m: ")
    weight = input("Enter your weight in kg: ")
    bmi = int(float(weight) / float(height) ** 2)
    print("Your BMI is: " + str(bmi))
