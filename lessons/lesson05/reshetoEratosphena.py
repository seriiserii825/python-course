def reshetoEratosphena():
    n = 40
    arr = [True] * n
    print(f'arr: {arr}')
    arr[0] = arr[1] = False

    for k in range(2, n):
        if arr[k]:
            for m in range(2*k, n, k):
                arr[m] = False
    for k in range(n):
        print(f'{k} - {"simple" if arr[k] else "not simple"}')



