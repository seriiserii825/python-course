def l_06_lambda_function():
    def greeting(greet: str):
        return lambda name: f"{greet}, {name}!"

    morning_greet = greeting("Good morning")
    evening_greet = greeting("Good evening")
    print(morning_greet("Alice"))
    print(evening_greet("Bob"))
