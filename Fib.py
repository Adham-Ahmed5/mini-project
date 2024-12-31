import random

# Function to merge two sorted sublists into one sorted list
def merge(left, right):
    sorted_list = []
    while left and right:
        if left[0] < right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    sorted_list.extend(left)  # Add remaining elements (if any)
    sorted_list.extend(right)
    return sorted_list

# Merge Sort function
def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: a list of length 0 or 1 is already sorted
    mid = len(arr) // 2  # Find the middle point
    left_half = merge_sort(arr[:mid])  # Recursively sort the left half
    right_half = merge_sort(arr[mid:])  # Recursively sort the right half
    return merge(left_half, right_half)  # Merge the sorted halves

# Generate a random list of numbers
random_list = [random.randint(1, 100) for _ in range(10)]  # List of 10 random integers between 1 and 100

print("Original List:")
print(random_list)

# Apply Merge Sort
sorted_list = merge_sort(random_list)

print("\nSorted List:")
print(sorted_list)
