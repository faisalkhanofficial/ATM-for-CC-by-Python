def get_amount():
    try:
        amt = int(input("Enter amount: "))
        return amt
    except:
        print("Invalid input! Enter a number.")
        return None