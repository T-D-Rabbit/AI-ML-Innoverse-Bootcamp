income=int(input("Please input your income: "))

expenses={}

for i in ["rent","food","travel","miscellaneous"]:
    amount=int(input(f"How much is spent on {i}? "))
    expenses[i]=amount

remaining=income-sum(expenses.values())

log=''

if remaining<=0:
    print(f"Please be careful! You are in the negative: {remaining}.")
    log+=f"User was advised to be careful, as user was in negative of {remaining}"
if remaining<1000:
    print(f"Please consider saving the remaining {remaining}")
    log+=f"User was advised to consider saving the remaining {remaining}"
else:
    print(f"Good job! You have a good amount remaining: {remaining}")
    log+=f"User has saved sufficiently: {remaining}. No comments."

with open("budget.txt",'w') as budget:
    budget.write(f"Income is {income}\n------\n")
    budget.write("Expenses are given as follows:\n")
    budget.write(f"---> Rent is {expenses['rent']}\n")
    budget.write(f"---> Food is {expenses['food']}\n")
    budget.write(f"---> Travel is {expenses['travel']}\n")
    budget.write(f"---> Miscellaneous spending is {expenses['miscellaneous']}\n\n")
    budget.write(f"User has {remaining} amount remaining. Further, comments log is as follows:\n--->")
    budget.write(log)

