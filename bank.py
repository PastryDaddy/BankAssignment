#"Account" class bank account management. Given needed parameters, this class provides tools for basic user operations.
class Account:
#this part of the code (Constructor?) dictates how to initialize the class, and establishes how the parameters are used within the class.
    def __init__(self, accountNumber, owner, balance):
        self.__accountNumber = str(accountNumber)
        self.__owner = str(owner)
        self.__balance = float(balance)

# this method simply returns all basic account info
    def getInfo(self):
        return f"Hello, {self.__owner}! For account {self.__accountNumber}, your current balance is {self.__balance}."

   # this method shows just the balance
    def getBalance(self):
        return f"Your balance is: {self.__balance}"
    
    # this method executes a deposit to the account, and deisplays the results of the operation
    def deposit(self, amount):
        amount = float(amount)
        self.__balance += amount
        return f"Deposited: {amount}, \nNew balance: {self.__balance}"
   # this method executes a withdrawal from the account, and displays the results of the operation 
    def withdraw(self, amount):
        amount = float(amount)
        if amount <= self.__balance:
                self.__balance -= amount
                return f"Withdrawn: {amount} \nNew Balance: {float(self.__balance)}"
        else:
                return "Error: Get your money up."
            
 # these are three example instances of bank accounts using the created class       
Group3A = Account(5374, "Erica", 778972)
Group3B = Account(9007, "Ryan", 542789)
Group3C = Account(3297, "Chris", 25)
# this is just a (helper?) function I looked up to help me validate the amount inputs
def numeric(i):
    try:
         float(i) 
         return True
    except ValueError:
        return False
#Here is the main program that people will actually use to manage their accounts. 
# This program relies on the Account class for functionality, and is kind of an interface between the class and the user. 
# I originally tried to implement a lot of the error handling in the class, but eventually realized I needed to put it in this "main" program instead. 
# So the class is really just the basic operations, and this is the rest.
def User(username):
    #At first I tried to build the whole thing out in a series of nested if statements, but then I realized that to get back to the beginning, 
    # handle errors, and provide more user-friendly experience, I should put mini-functions(Methods?) inside the big functon. 
    # This way I can just make them call themselves or eachother for smoother navigation and less clutter.
    #This first handles deposits, and all potential outcomes for users.
    def deposit():
        #finding out how much user wants to deposit
        amount = float(input("How much would you like to deposit?"))
        #using helper function to handle errant inputs
        if numeric(amount):
            # calling on the class to handle the actual deposit operation
            if amount >= 0:
                print(username.deposit(amount)) 
                #giving user option to go back to welcome screen
                more()
                # in case user enters a negative number, which is technically a withdrawal...
            else:
                # I had to look up the abs() thing. also I tried to write "username._Account__balance" like 35 different ways before I looked up how to write it correctly. 
                # I think it's so complicated to write it that way only because of the protected parameters of the class?
                #also here, I make sure that before i give option to withdraw, I make sure the amount would even be a valid withdrawal
                if abs(amount) <= username._Account__balance:
                    #giving option to treat negative deposit as withdrawal
                    withdrawal = input(f"Cannot deposit negative amount. Would you like to withdraw {abs(amount)}? (y/n)")
                    if withdrawal.lower() == "y":
                        print(username.withdraw(abs(amount)))
                        more()
                    elif withdrawal.lower() == "n":
                        print("Please enter a positive amount.")
                        deposit()
                        #input validation
                    else:
                         print("Invalid input. Please try again.")
                         User(username)
                else: 
                    print("Cannot deposit negative amount.")
                    deposit()
        else:
             print("Please enter your deposit amount in numerals.")
             deposit()
        
#This is the withdrawal function, basically the same as deposit, just opposite.
    def draw():
        amount = float(input("How much would you like to withdraw?"))
        if numeric(amount):
            if amount >= 0:
                print(username.withdraw(amount))
                more()
            else:
                dep = input(f"Cannot withdraw negative amount. Would you like to deposit {abs(amount)}? (y/n)")
                if dep.lower() == "y":
                    print(username.deposit(abs(amount)))
                    more()
                elif dep.lower() == "n":
                    print("Please enter a positive amount.")
                    draw()
                else:
                    print("Invalid input. Please try again.")
                    User(username)
        else:
             print("Please enter your withdrawal amount in numerals.")
             draw()
        
        
# this just calls on the class to display the account info
    def info():
        print(username.getInfo())
        more()
        
   # same, but just for the balance     
    def balance():
        print(username.getBalance())
        more()

   # a method I created so I wouldn't have to keep writing the same if statement over and over in the other methods
    def more():
        option = input("Would you like to do anything else? (y/n)")
        if option.lower() == "y":
            User(username)
        else:
            print("Thanks for banking with us! Goodbye!")
# the welcome "screen" for the program. Initially I had this at the beginning, but the methods didn't work until I put it at the bottom. Why is that?
    menu = input(f"Hello, {username._Account__owner}! What would you like to do today? \n1. Deposit\n2. See Your Balance\n3. View Account Info\n4. Withdraw")
    if menu.lower() == "1":
            deposit()
    elif menu.lower() == "2":
            balance()
    elif menu.lower() == "3":
            info()
    elif menu.lower() == "4":
            draw()
    else:
         print("Please choose 1, 2, 3, or 4.")
         User(username)
        
        
      

User(Group3A)



    