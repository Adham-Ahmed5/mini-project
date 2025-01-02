def calculate_average(numbers):
    # Check if the list is empty to avoid division by zero
    if len(numbers) == 0:
        return 0
    # Calculate the sum of the list
    total_sum = sum(numbers)
    # Calculate the average by dividing the sum by the length of the list
    average = total_sum / len(numbers)
    return average

# Example usage:
numbers = [10, 20, 30, 40, 50]
print(f"The average is: {calculate_average(numbers)}")
