import random
lowest = 0
highest = 100
running = True
while running:
    answer=random.randint(lowest,highest)
    gueses = 0
    guess = int(input())
    if guess is int ():
        gueses+=1
    if guess in range (lowest,highest):
        print("out of range")
    elif guess<answer:
        print("Too low")
    elif guess > answer:
        print("Too high")
    else:
        (f"correct:{answer}")
    print(f"{gueses}")
    
    play_again = input("would you like to play again?(y/n):").lower()
    if not play_again =="y":
        running = False
else:
    print("Invalid")
play_again = input("would you like to play again?(y/n):").lower()
if not play_again =="y":
        running = False
print("---Thanks for playing!---")

        