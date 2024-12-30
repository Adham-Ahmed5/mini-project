def calculate_factorial(n):
    # Initialize result to 1 (since factorial of 0 is 1)
    result = 1
    
    # Loop from 1 to n (inclusive) to calculate the factorial
    for i in range(1, n + 1):
        result *= i  # Multiply result by the current number i
    
    return result

def main():
    # Take user input for the number
    while True:
        try:
            number = int(input("Enter a number to calculate its factorial: "))
            if number < 0:
                print("Please enter a non-negative integer.")
                continue
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    
    # Calculate the factorial using the function
    factorial = calculate_factorial(number)
    
    # Print the result
    print(f"The factorial of {number} is: {factorial}")

# Run the program
if __name__ == "__main__":
    main()

