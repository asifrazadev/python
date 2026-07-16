# Advanced Exception Handling: Raise and Finally in Python

# Custom Exception inheriting from Exception
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Attempted to withdraw ${amount} but balance is only ${balance}.")
        self.balance = balance
        self.amount = amount

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                # Raising a custom exception
                raise InsufficientFundsError(self.balance, amount)
            self.balance -= amount
            print(f"Successfully withdrew ${amount}. New balance: ${self.balance}")
        except InsufficientFundsError as e:
            # Handle error
            print(f"Transaction Failed: {e}")
            raise  # Re-raise the error if we want it to bubble up
        finally:
            # This block ALWAYS runs, used for resource cleanup
            print(f"Transaction attempt completed for {self.owner}.\n")

# Test BankAccount
acc = BankAccount("Alice", 100)

# Successful transaction
acc.withdraw(40)

# Unsuccessful transaction (will raise and handle the exception)
try:
    acc.withdraw(150)
except InsufficientFundsError:
    print("Caught re-raised exception in main program flow.")
