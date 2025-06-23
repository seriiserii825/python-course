def l_05_extract_dict():
    button = {
        "color": "white",
        "background": "blue",
    }

    red_button = {
        **button,
        "background": "red",
    }

    # background will be overwritten

    print(f'{red_button}: red_button')
    # {'color': 'white', 'background': 'red'}: red_button

    button_1 = {
        "color": "white",
        "background": "blue",
    }

    button_2 = {
        "font-size": "12px",
        "border-radius": "5px",
    }

    my_button = {
        **button_1,
        **button_2,
    }
    # my_button will contain all keys from both dictionaries

    # or union operator
    my_button = button_1 | button_2
    print(f"my_button: {my_button}")
