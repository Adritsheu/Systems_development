#!/usr/bin/python3

#Problem 3

from enum import Enum
class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2
    
    
class BankAccount():
    
    def __init__(self, owner, accountType: AccountType):
        # your code
        self.balance = 0
        self.owner = owner
        self.accountType = accountType

    def withdraw(self, amount):
        # your code
        if amount > self.balance:
            raise ValueError("You are taking out more than whats in your balance")
        elif amount < 0:
            raise ValueError("You need to take out more than zero")
        else:
            self.balance = self.balance - amount
        
        
    def deposit(self, amount):
        # your code
        if amount < 0:
            raise ValueError("You need to add more than zero")
        else:
            self.balance = self.balance + amount

    def __str__(self):
        # your code
        account_type = self.accountType.name
        return f"The owner of this account is: {self.owner}.This has the account type:{account_type}"

    def __len__(self):
        # your code
        return self.balance
 

 # Part B: creating new class
    
class BankUser():
    
    def __init__(self, owner):
        self.owner = owner
        self.accounts = []
        self.Savings = None
        self.Checking = None
        
    def addAccount(self, accountType):
        if accountType == AccountType.SAVINGS:
            if self.Savings == None:
                self.Savings = BankAccount(self.owner, accountType)
                self.accounts.append(accountType.name)
            else:
                raise Exception(f"You already have a {accountType.name} Account")
                
        elif accountType == AccountType.CHECKING:
            if self.Checking == None:
                self.Checking = BankAccount(self.owner, accountType)
                self.accounts.append(accountType.name)
            else:
                raise Exception(f"You already have a {accountType.name} Account")
            
            
    def getBalance(self, accountType):
        if accountType == AccountType.SAVINGS:
            if self.Savings == None: # not means not NONE
                raise Exception("You do not have a Saving account.") #EXIT THE function
            return self.Savings.balance
        
        
        elif accountType == AccountType.CHECKING:
            if self.Checking != None:
                return self.Checking.balance
            else:
                raise Exception("You do not have a Checking account.")
            
        
    
    
    def deposit(self, accountType, amount):
        if accountType == AccountType.SAVINGS:
            if self.Savings == None:
                raise Exception("You do not have a Savings account.")
            return self.Savings.deposit(amount)
            
        elif accountType == AccountType.CHECKING:
            if self.Checking == None:
                raise Exception("You do not have a Checking account.")
            return self.Checking.deposit(amount)
            
    
    
    def withdraw(self, accountType, amount):
        if accountType == AccountType.SAVINGS:
            if self.Savings == None:
                raise Exception("You do not have any Saving accounts.")
            return self.Savings.withdraw(amount)
        
        elif accountType == AccountType.CHECKING:
            if self.Checking == None:
                raise Exception("You do not have any Checking accounts.")
            return self.Checking.withdraw(amount)
      
    def __str__(self):
        if self.Savings != None and self.Checking == None: return "You have a Savings Account and no Checking."
        elif self.Savings == None and self.Checking == None: return "You do not have a Savings of Checking Account"
        elif self.Checking != None and self.Savings == None: return "You have a Checkings Account and no Savings Account"
        elif self.Checking != None and self.Savings != None: return "You have both Checkings and Savings Account"
        
            
# Part 3C:

def ATMSession(bankUser: BankUser):
    #2print("In atm sess")
    
    def Interface(bankUser):
        #print("Interface")

        ## Need while loop = True
        while True:
            print("Enter Option: \n"
            "1) Exit \n"
            "2) Create Account \n"
            "3) Check Balance \n"
            "4) Deposit \n"
            "5) Withdraw \n")
            answer = input()
             

            try:

                ## Exiting
                if answer == "1":
                    break
                    

                ## Creating an account
                elif answer == "2":
                    print("Enter Option: \n"
                          "1) Checking \n"
                          "2) Savings \n")
                    account = input()
                    
                    
                      # Checking Account
                    if account == "1":
                        user.addAccount(AccountType.CHECKING);
                        print(str(user)) # same


                    # Savings Account
                    elif account == "2":
                        user.addAccount(AccountType.SAVINGS);
                        print(str(user)) #same

                  

                ## Checking Balance
                elif answer == "3":
                    print("Enter Option: \n"
                          "1) Checking \n"
                          "2) Savings \n")
                    account = input()

                    if account == "2":
                        print(user.getBalance(AccountType.SAVINGS))
                    else:
                        print(user.getBalance(AccountType.CHECKING))




                ## Depositing or Withdrawals:  4 = Deposit 5 = withdraw
                elif answer == "4" or answer == "5":

                    print("Enter Option: \n"
                          "1) Checking \n"
                          "2) Savings \n")
                    account = input()


                    print("Enter integer amount that is nonnegative")
                    new_am = int(input())

                    #Deposits
                    if answer == "4" and account == "2":
                        user.deposit(AccountType.Savings, new_am)
                        print(user.getBalance(AccountType.SAVINGS))

                    elif answer == "4" and account == "1":
                        user.deposit(AccountType.CHECKING, new_am)
                        print(user.getBalance(AccountType.CHECKING))

                    #Withdrawals
                    elif answer == "5" and account == "2":
                        user.withdraw(AccountType.SAVINGS, new_am)
                        print(user.getBalance(AccountType.SAVINGS))
                    elif answer == "5" and account == "1":
                        user.withdraw(AccountType.CHECKING, new_am)
                        print(user.getBalance(AccountType.CHECKING))

            except Exception as e:
                print(e)
    return Interface(bankUser)
            


            
user = BankUser("Joe")
ATMSession(user)
