#Means hiding internal details of a class and only exposing what's necessary.
#Binding data and methods together in a class and restricting direct access to some of the data.
#HELPS TO:
#Protect sensitive data
#Prevent accidental changes
#Improve security


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance   # Private variable (encapsulated)

    # Getter method
    def get_balance(self):
        return self.__balance

    # Setter method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount")


# Creating object
account = BankAccount("Ruby", 1000)

# Accessing balance using getter
print("Current balance:", account.get_balance())

# Depositing money
account.deposit(500)

# Withdrawing money
account.withdraw(300)

# Trying to access private variable directly (will cause error)
# print(account.__balance)   # ❌ Not allowed

    #EXPLANATION
#__balance is a private variable (notice the double underscore __).
#It cannot be accessed directly outside the class.
#We use public methods (get_balance, deposit, withdraw) to access or modify it.
#This protects the data and controls how it is changed.