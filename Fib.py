def factorial(n):
    # Base condition: When n is 1 or 0, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive return: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

def main():
    number = int(input("Enter a number to calculate its factorial: "))
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")

# Call the main function to run the program
main()
