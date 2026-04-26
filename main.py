from services.atm_service import get_balance, deposit, withdraw, get_statement
from utils.helper import get_amount

def atm_menu():
    while True:
        print("\n====== ATM MENU ======")
        print("1. Display Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Statement")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current Balance: Rs", get_balance())

        elif choice == "2":
            amt = get_amount()
            if amt is not None:
                print(deposit(amt))

        elif choice == "3":
            amt = get_amount()
            if amt is not None:
                print(withdraw(amt))

        elif choice == "4":
            print("\n--- Transaction History ---")
            for t in get_statement():
                print(t)

        elif choice == "5":
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice. Try again.")


# Start program
atm_menu()