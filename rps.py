import random
running = True
options =("rock", "paper", "scissors")

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice(rock,paper,scissors):")
        
    print(f"player:{player}")
    print(f"computer:{computer}")
    if player == computer:
        print("a draw")
    elif player == "rock" and computer == "scissors":
            print ("You win")
    elif player == "paper" and computer == "rock":
            print ("You win")
    elif player == "scissors" and computer == "paper":
        print ("You win")
    else:
            print("You lose")    
            
    play_again = input("would you like to play again?(y/n):").lower()
    if not play_again =="y":
        running = False
        
print("---Thanks for playing!---")

    
