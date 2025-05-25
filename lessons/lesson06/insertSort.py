def insertSort():
    """
    This function implements the insertion sort algorithm.
    It sorts a list of numbers in ascending order.
    """
    my_arr = [5, 2, 9, 1, 5, 6]
    print(f"my_arr: {my_arr}")
    def test1(arr):
        n = len(arr) # Get the length of the array
        for top in range(1, n):
            k = top # Start with the second element
            while k > 0 and arr[k - 1] > arr[k]:
                # If the previous element is greater, swap them
                arr[k - 1], arr[k] = arr[k], arr[k - 1]
                k -= 1
    test1(my_arr)
    print(f"Sorted my_arr: {my_arr}")

