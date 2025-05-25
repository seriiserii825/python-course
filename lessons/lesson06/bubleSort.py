def bubleSort():
    my_arr = [5, 2, 9, 1, 5, 6]
    print(f"my_arr: {my_arr}")

    def test1(arr):
        """ Bubble Sort Algorithm""" 
        n =len(arr)
        for bypass in range(1, n):
            for i in range(0, n - bypass):
                if arr[i] > arr[i + 1]:
                    # Swap the elements
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
    print(f"my_arr: {my_arr}")
