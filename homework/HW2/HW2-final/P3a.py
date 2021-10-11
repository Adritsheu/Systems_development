# Part 3a: 

#!/usr/bin/python3

print("This does not behave correctly because when you pass a new withdrawal amount it uses the initial balance that was set. It should save out what the new balance is and replace our initial balance after every withdrawal. ")

def make_withdrawal(init_balance): 
    print(f"Here is the starting balance {init_balance}")
    def withdrawal_amount(amt):
        if amt > init_balance:
            return print("You are exceeding your initial balance. Please try to withdrawal a smaller amount")
        else:
            new_bal = init_balance - amt
        return new_bal              
    return withdrawal_amount

wd = make_withdrawal(100)
print(f"Our first initial withdrawl is 20 and are left with {wd(20)}") # starting from 100
print(f"Our second initial withdrawl is 80 and are left with {wd(80)}") #starting from 100 when we would want it to be 80


