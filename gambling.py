# ______SLOT MACHINE GAME______
import random


def spin_row():
    symbols = ["🍒", "🍋", "🔔", "⭐", "7️⃣"]
    result = []
    for symbol in range(3):
        result.append(random.choice(symbols))
    return result


def print_row(row):
    print("*****************")
    print(" | ".join(row))
    print("*****************")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "7️⃣":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 3
        elif row[0] == "🍋":
            return bet * 2
        elif row[0] == "🍒":
            return bet * 1
    return 0


def main():
    balance = 100.0
    print("***********************")
    print("** Welcome to Slots! **")
    print("symbols: 🍒, 🍋, 🔔, ⭐, 7️⃣")
    while balance > 0:
        print(f"Current balance: ${balance:.2f}")
        bet = float(input("Enter your bet amount (or 0 to quit): $"))
        if bet <= 0:
            print("------Thanks for playing! Goodbye.----")
            break
        elif bet > balance:
            print("Insufficient balance. Please enter a valid bet.")
            continue
        row = spin_row()
        print("Spinning...👍👍")
        print_row(row)
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"Congratulations! You won ${payout:.2f}!")
            balance += payout
        else:
            print("Sorry, you lost this round.")
            balance -= bet
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            print("------Thanks for playing! Goodbye.----")
            break
        print("-----------------------")


print("Game over! Your final balance is: ${balance:.2f}")
if __name__ == "__main__":
    main()
