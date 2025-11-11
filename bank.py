# _____Banking program_______
def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")


def deposit():
    amount = float(input("Enter amount to deposit: $"))
    if amount < 0:
        print("Deposit amount must be more than 0.")
        return 0.0
    else:
        return amount


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: $"))
    if amount > balance:
        return 0.0
        print("insufficient funds.")
    elif amount < 0:
        print("amount must be more than 0.")
        return 0.0
    else:
        return amount


def main():
    balance = 0.0
    running = True
    while running:
        print("\n----- BANKING PROGRAM -----")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            amount = deposit()
            balance += amount
            print(f"${amount:.2f} deposited.")
        elif choice == "3":
            amount = withdraw(balance)
            if amount > 0:
                balance -= amount
                print(f"${amount:.2f} withdrawn.")
        elif choice == "4":
            print("Exiting program. Goodbye!")
            running = False
            break
        else:
            print("Invalid choice. Please select a valid option.")


print("-----------Thank you for using our services----.")
if __name__ == "__main__":
    main()
