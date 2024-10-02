# Chapter 9 Classes and Objects

# 9.1 
# Create a class called Cat. The class should have the following attributes:
# name, age, color
class Cat:
    def __init__(self, name) -> None:
        self.name = name



# 9.2
# create a cat object and print the name, age, and color of the cat
# use the following values for the cat object:
# name: Whiskers
# age: 3
# color: black
#return the cat object
def create_cat():
    raise NotImplementedError("9.2")



# 9.3 
# Create a new class, then change the age of the cat to 4 after the cat object is created
def change_cat_age(cat):
    #my_cat = Cat("Whiskers", 3, "black")
    raise NotImplementedError("9.3")


# 9.4
# Create a class called BankAccount. The class should have the following attributes:
# account_number, account_holder, balance
# The class should only use account number account holder in the initialization method
# The balance should be set to 0 in the initialization method
# The initializer method is the __init__ method
class BankAccount:
    def __init__():
        raise NotImplementedError("9.4")

# 9.5
# Create a bank account object and print the account number, account holder
# The bank account object should use the following values:
# account number: 123456
# account holder: Mr. Wilmoth
# return the bank account object

def create_bank_account():
    raise NotImplementedError("9.5")

# 9.6
# Copy and paste your class from 9.4.
# Remame the class BankAccount to BankAccount2
# Add a method to the class called deposit
# The method should take an argument called amount
# The method should add the amount to the balance
# The method should return the new balance
class BankAccount2:
    def __init__():
        raise NotImplementedError("9.4")


# 9.7
# Copy and paste your class from 9.6
# Rename the class BankAccount2 to BankAccount3
# Add a method to the class called withdraw
# The method should take an argument called amount
# The method should subtract the amount from the balance
# The method should return the new balance
# The method should not allow the balance to go below 0
# If the balance goes below 0, use this error:
# raise ValueError("Insufficient funds for withdrawal.")
class BankAccount3:
    def __init__():
        raise NotImplementedError("9.4")

# 9.8
# Create a bank account object using the BankAccount3 class
# Use the following values:
# account number: 314159
# account holder: Mr. Orlando
# deposit 100
# withdraw 50
# withdraw 100
# return the bank account object
def create_bank_account3():
    raise NotImplementedError("9.8")

