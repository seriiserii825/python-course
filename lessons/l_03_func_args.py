def l_03_func_args():
    def sum_nums(*args):
        print(args)  # tuple(1, 2, 3)
        return sum(args)

    # named args
    def get_posts_info(name, posts_qty):
        print(f"Name: {name}, Posts Quantity: {posts_qty}")

    get_posts_info(name="John", posts_qty=5)

    # **args
    def get_cars_info(**kwargs):
        print(kwargs)  # {'name': 'Ford', 'model': 'Focus', 'year': 2020}

    get_cars_info(name="Ford", model="Focus", year=2020)
