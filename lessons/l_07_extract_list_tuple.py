def l_07_extract_list_tuple():
    my_list = [1, 2, 3, 4, 5]
    first, second, third, fourth, fifth = my_list
    print(
        f"First: {first}, Second: {second},\
        Third: {third}, Fourth: {fourth}, Fifth: {fifth}"
    )

    my_tuple = (10, 20, 30, 40, 50)
    first_tuple, second_tuple, *rest_of_tuple = my_tuple
    print(f"{first_tuple}: first_tuple")
    print(f"{second_tuple}: second_tuple")
    print(f"{rest_of_tuple}: rest_of_tuple")

    user_profile = {
        "name": "Alice",
        "comments_qty": 5,
    }

    def user_info(name, comments_qty=0):
        if not comments_qty:
            return f"User {name} has no comments."
        return f"User {name} has {comments_qty} comments."

    # print(user_info(user_profile['name'], user_profile['comments_qty']))
    print(user_info(**user_profile))

    suer_data = ["Bob", 10]

    def user_data(name, comments_qty=0):
        if not comments_qty:
            return f"User {name} has no comments."
        return f"User {name} has {comments_qty} comments."

    # print(user_data(suer_data[0], suer_data[1]))
    print(user_data(*suer_data))
