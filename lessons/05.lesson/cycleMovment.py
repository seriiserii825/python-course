def cycleMovment():
    my_arr = [0, 1, 2, 3 ,4]
    def moveLeft(A: list):
        print(f'A: {A}')
        arr_len = len(A)
        tmp = A[0]
        for i in range(arr_len - 1):
            A[i] = A[i + 1]
        A[arr_len - 1] = tmp
        print(f'A: {A}')

    def moveRight(B: list):
        print(f'B: {B}')
        arr_len = len(B)
        tmp = B[arr_len - 1]
        for i in range(arr_len):
            if i == 0:
                B[i] = tmp
            else:
                B[i] = B[i]
        print(f'B: {B}')

    ar_1 = list(my_arr)
    ar_2 = list(my_arr)
    moveLeft(ar_1)
    moveRight(ar_2)
