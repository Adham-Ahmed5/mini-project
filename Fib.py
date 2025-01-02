def fibonacci(n):
    # Base cases: fibonacci(0) = 0 and fibonacci(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive call: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    # Input from the user to calculate the nth Fibonacci number
    number = int(input("Enter the Fibonacci sequence index: "))
    
    # Calculate the Fibonacci number
    result = fibonacci(number)
    
    # Print the result
    print(f"The Fibonacci number at index {number} is: {result}")

# Call the main function to run the program
main()
