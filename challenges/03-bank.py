
balance = 0

def check_balance():
    print(f"Your current balance is ${balance}")

def deposit():
    if int(amount) < 0:
        return
    global balance
    balance += int(amount)
    print(f"Your new balance is ${amount}.")

def withdraw():
    amount = input("How much would you like to withdraw?\n")
    if int(amount) < 0:
        print(f'ERROR, please type in correct amount')
    elif int(amount) > balance:
        print("You do not have enough for this amount.")
        return
    print(f"You have withdrawn ${amount}.")


while not done:
    action = input("What would you like to do? (deposit, withdraw, check balance)\n")

    if action == "deposit":
        deposit()
    elif action == "withdraw":
        withdraw()
    elif action == "check balance":
        check_balance()
    else:
        print("Thank you!")
        return


print("Have a nice day!")