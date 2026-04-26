from data.atm_data import balance, transactions

def get_balance():
    return balance


def deposit(amount):
    global balance
    if amount <= 0:
        return "Invalid amount"

    balance += amount
    transactions.append(f"Deposited: Rs {amount}")
    return "Deposit Successful"


def withdraw(amount):
    global balance
    if amount <= 0:
        return "Invalid amount"

    if amount > balance:
        return "Insufficient Balance"

    balance -= amount
    transactions.append(f"Withdrawn: Rs {amount}")
    return "Withdrawal Successful"


def get_statement():
    if not transactions:
        return ["No transactions yet"]
    return transactions