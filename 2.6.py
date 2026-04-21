balance = 3000000

def deposit(amount):
    global balance
    balance += amount
    print("Deposited:", amount)

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print("Withdrawn:", amount)

def check_balance():
    print("Current Balance:", balance)



deposit(1000)
withdraw(300)
check_balance()
