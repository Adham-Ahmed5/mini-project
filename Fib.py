import random

def insertion_sort(arr):
    """
    Sorts an array using the insertion sort algorithm.

    Args:
      arr: The list of numbers to be sorted.

    Returns:
      The sorted list.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Create a random list of numbers
data = [random.randint(1, 100) for _ in range(10)] 
print("Unsorted List:", data)

# Sort the list using insertion sort
sorted_data = insertion_sort(data)
print("Sorted List:", sorted_data)