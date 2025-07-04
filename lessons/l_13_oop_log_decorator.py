def l_13_oop_log_decorator():
    def log_function_call(fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            func_name = fn.__name__
            print(f"Function '{func_name}' called with arguments: {args}, {kwargs}")
            func_args = ", ".join(map(str, args))
            print(f"Arguments: {func_args}")
            print(f"Result: {result}")
            return result

        return wrapper

    @log_function_call
    def mult(a, b):
        return a * b

    mult(2, 3)
