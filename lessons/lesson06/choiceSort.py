def choiceSort():
  """ Choice Sort Algorithm"""
  arr = [5, 2, 9, 1, 5, 6]
  n = len(arr)

  for i in range(n):
    # Find the minimum element in remaining unsorted array
    min_idx = i # Assume the first element is the minimum
    for j in range(i + 1, n): # Traverse the unsorted part
      if arr[j] < arr[min_idx]: # If a smaller element is found
        min_idx = j # Update the index of the minimum element

    # Swap the found minimum element with the first element
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

  return arr
