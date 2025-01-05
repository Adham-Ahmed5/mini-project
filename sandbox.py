import os

class BankAccount:
    def __init__(self, username, account_type, balance=0):
        """Constructor to create a new bank account."""
        self.username = username
        self.account_type = account_type
        self.balance = balance
        self.account_id = self.generate_account_id()
        
        # Create a transaction file for the user
        self.filename = f"{self.username}_{self.account_type}_{self.account_id}_statement.txt"
        self.create_transaction_file()
    
    def generate_account_id(self):
        """Generate a unique account ID."""
        # For simplicity, we just generate an ID based on the name's length and a random number.
        return hash(self.username) % 100000
    
    def create_transaction_file(self):
        """Create a new file for the user's transactions."""
        with open(self.filename, 'w') as file:
            file.write("Transaction History for account: " + str(self.account_id) + "\n")
            file.write("Account Type: " + self.account_type + "\n")
            file.write("Account Balance: $" + str(self.balance) + "\n")
            file.write("="*40 + "\n")
    
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            self.log_transaction(f"Deposited: ${amount}")
            print(f"Deposited ${amount} successfully.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= self.balance:
            self.balance -= amount
            self.log_transaction(f"Withdrew: ${amount}")
            print(f"Withdrew ${amount} successfully.")
        else:
            print("Insufficient balance!")
    
    def log_transaction(self, transaction_details):
        """Log each transaction in the user's transaction file."""
        with open(self.filename, 'a') as file:
            file.write(transaction_details + "\n")
    
    def get_balance(self):
        """Return the current balance of the account."""
        return self.balance
    
    def get_account_id(self):
        """Return the account ID."""
        return self.account_id
    
    def get_username(self):
        """Return the username (account holder name)."""
        return self.username
    
    def get_account_type(self):
        """Return the account type (e.g., Chequing, Savings)."""
        return self.account_type
    
    def get_transaction_history(self):
        """Retrieve and display the transaction history from the user's file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return file.read()
        else:
            return "Transaction file does not exist."


# Testing the BankAccount class

# Create a few bank account objects
account1 = BankAccount("Alice", "Savings", 500)
account2 = BankAccount("Bob", "Chequing", 1000)

# Perform some operations
account1.deposit(200)
account1.withdraw(50)

account2.deposit(500)
account2.withdraw(1500)  # Attempt to withdraw more than balance

# Print out balances
print(f"Alice's Balance: ${account1.get_balance()}")
print(f"Bob's Balance: ${account2.get_balance()}")

# Print transaction history
print("\nAlice's Transaction History:")
print(account1.get_transaction_history())

print("\nBob's Transaction History:")
print(account2.get_transaction_history())

# Retrieve and print account details
print("\nAccount Details:")
print(f"Alice's Account ID: {account1.get_account_id()}")
print(f"Alice's Account Type: {account1.get_account_type()}")

