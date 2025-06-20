def l_03_func_args():
    def sum_nums(*args):
        print(args)  # tuple(1, 2, 3)
        return sum(args)
