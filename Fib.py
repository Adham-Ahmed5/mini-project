def is_prime(n):
    # A prime number is greater than 1 and divisible only by 1 and itself
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # If n is divisible by any number other than 1 and itself
            return False
    return True

def main():
    # Take user input
    while True:
        try:
            num = int(input("Enter a number to find prime numbers up to that number: "))
            if num < 2:
                print("Please enter a number greater than or equal to 2.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    
    print(f"Prime numbers up to {num}:")
    
    # Loop through all numbers from 2 to the user's number and print primes
    for i in range(2, num + 1):
        if is_prime(i):
            print(i, end=" ")

# Run the program
if __name__ == "__main__":
    main()
