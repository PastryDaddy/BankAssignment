# Account Class Documentation

## Class Description

The Account class provides basic tools for user account management

## Attributes

- __accountNumber (str): The account number of the account.
- __owner (str): The owner of the account.
- __balance (float): The balance of the account.

### __init__(self, accountNumber, owner, balance)

Constructor to initialize an instance of Account 

- **Parameters:**
  - accountNumber (str): The account number.
  - owner (str): The owner of the account.
  - balance (float): The current account balance.

## Methods

### getInfo(self)

Returns a string with basic account information.

- **Returns:**
  - str: Account owner, account number, and balance.

### getBalance(self)

Returns the current account balance.

- **Returns:**
  - str: A string containing the account balance.

### deposit(self, amount)

Deposits the specified amount into the account.

- **Parameters:**
  - amount (float): The amount to be deposited.

- **Returns:**
  - str: A string containing the deposit and the new balance.

### withdraw(self, amount)

Withdraws the specified amount from the account.

- **Parameters:**
  - amount (float): The amount to be withdrawn.

- **Returns:**
  - str: A string containing the withdrawal and the new balance, or an error message if the amount exceeds the balance.

## Example Usage


# Creating an instance of the Account class
account = Account(5374, "Erica", 778972)

# Getting account information
print(account.getInfo())  # Output: Hello, Erica! For account 5374, your current balance is 778972.0.

# Checking balance
print(account.getBalance())  # Output: Your balance is: 778972.0

# Depositing money
print(account.deposit(500))  # Output: Deposited: 500.0, New balance: 779472.0

# Withdrawing money
print(account.withdraw(200))  # Output: Withdrawn: 200.0, New Balance: 779272.0
