def l_08_forin():
    my_dict = {
        "name": "Alice",
        "age": 30,
    }

    # for item in my_dict.items():
    #     key, value = item
    #     print(f"{key}: {value}")

    for key, value in my_dict.items():
        print(f"{key}: {value}")

    my_list = ["apple", "banana", "cherry"]

    for index, value in enumerate(my_list):
        print(f"Index: {index}, Value: {value}")
