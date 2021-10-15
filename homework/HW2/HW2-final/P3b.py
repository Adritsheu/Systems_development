# Part 3b: Disclosures & Decorators
# must write a bank account statement
# need a nested function

#!/usr/bin/python3

print("The error is that the variable initial balance is saved as a local variable from our outer function that can only be read by the inner one. The nested function is unable to change it because it is outside the scope of the function. We did not have the error in the above example (3a) because we are able to read initial balance to create the new balance variable. In order to fix this we must set the initial balance as a non local variable.")


def make_withdrawal(init_balance): 
    print(f"Here is the starting balance {init_balance}")
    def withdrawal_amount(amt):
        if amt > init_balance:
            return print("You are exceeding your initial balance. Please try to withdrawal a smaller amount\n")
        else:
            init_balance = init_balance - amt
        return init_balance              
    return withdrawal_amount

#Using the practice inputs that I used before
wd = make_withdrawal(100)
print(wd(20))
print(wd(80))


