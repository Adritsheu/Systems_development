# Part 3c: Adding nonlocal 
#!/usr/bin/python3

def make_withdrawal(init_balance): 
    print(f"Here is the starting balance {init_balance}")
    def withdrawal_amount(amt):
        nonlocal init_balance
        if amt > init_balance:
            return print("You are exceeding your initial balance. Please try to withdrawal a smaller amount\n")
        else:
            init_balance = init_balance - amt
        return init_balance              
    return withdrawal_amount

wd = make_withdrawal(100)
print(f"Our initial withdrawal is 20 and we are left with {wd(20)}") #shows we get to 80
print(f"Our next withdrawal is 80 and we are left with {wd(80)}")# shows now we get to 0 because initial balance is updated

'''Permanent link to my python tutor: https://pythontutor.com/visualize.html#code=def%20make_withdrawal%28init_balance%29%3A%20%0A%20%20%20%20print%28f%22Here%20is%20the%20starting%20balance%20%7Binit_balance%7D%22%29%0A%20%20%20%20def%20withdrawal_amount%28amt%29%3A%0A%20%20%20%20%20%20%20%20nonlocal%20init_balance%0A%20%20%20%20%20%20%20%20if%20amt%20%3E%20init_balance%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20print%28%22You%20are%20exceeding%20your%20initial%20balance.%20Please%20try%20to%20withdrawal%20a%20smaller%20amount%5Cn%22%29%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20init_balance%20%3D%20init_balance%20-%20amt%0A%20%20%20%20%20%20%20%20return%20init_balance%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20return%20withdrawal_amount%0A%20%20%20%20%0Awd%20%3D%20make_withdrawal%28100%29%0Awd%2820%29%0Awd%2880%29&cumulative=false&curInstr=18&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false'''
