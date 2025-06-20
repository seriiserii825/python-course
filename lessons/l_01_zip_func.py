def l_01_zip_func():
    fruits = ['apple', 'banana', 'cherry']
    quantity = [100, 200, 300]
    avalability = (True, False, True)
    zipped = zip(fruits, quantity, avalability)

    zip_array = list(zipped)
    print(f"zip_array: {zip_array}")
    # zip_array: [('apple', 100, True), ('banana', 200, False), ('cherry', 300, True)]

    keys = ['fruit', 'quantity', 'avalability']
    values = ('apple', 100, True)

    zipped_dict = dict(zip(keys, values))
    print(f"zipped_dict: {zipped_dict}")
    # zipped_dict: {'fruit': 'apple', 'quantity': 100, 'avalability': True}
