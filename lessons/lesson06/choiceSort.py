def choiceSort():
    """ Choice Sort Algorithm"""
    my_arr = [5, 2, 9, 1, 5, 6]
    print(f"my_arr: {my_arr}")
    def test1(arr):
      n = len(arr)  # Get the length of the array
      for pos in range(0, n -1):
          for i in range(pos + 1, n): # Iterate through the unsorted part of the array
              if arr[i] < arr[pos]: # If the current element is smaller than the element at pos
                  # Swap the elements
                  arr[i], arr[pos] = arr[pos], arr[i] # Swap the elements

    test1(my_arr)
    print(f"Sorted my_arr: {my_arr}")
