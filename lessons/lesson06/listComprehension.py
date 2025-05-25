def listComprehension():
    b = []
    a = [1, 2, 3, 4, 5]
    for i in a:
        if i % 2 == 0:
            b.append(i**2)

    print(f'a: {a}')
    print(f'b: {b}')

    c = [ i**2 if i > 0 else 0 for i in a if i % 2 == 0]
    print(f"c: {c}")
