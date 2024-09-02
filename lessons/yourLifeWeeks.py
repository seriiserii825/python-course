def yourLifeWeeks():
    age = int(input("What is your current age? "))
    years = 90 - age
    months = years * 12
    weeks = years * 52
    days = years * 365
    print(f"You have {days} days, {weeks} weeks, {months} months and {years} years left.")
