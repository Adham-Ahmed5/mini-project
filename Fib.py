import random

# Function to implement Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to detect if any swapping occurs
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:  # Compare adjacent elements
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap if in wrong order
                swapped = True
        # If no elements were swapped, the list is sorted
        if not swapped:
            break

# Generate a random list of numbers
random_list = [random.randint(1, 100) for _ in range(10)]

print("Original List:")
print(random_list)

# Apply Bubble Sort
bubble_sort(random_list)

print("\nSorted List:")
print(random_list)
