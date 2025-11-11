import random
#print("\u25CF \u250C \u2510 \u2502 \u2514 \u2518")
dice_art = {
    1: ("┌----------------┐"
        "|                |"
        "|       ●        |"
        "|                |"
        "|                |"
        "└----------------┘"),
    2: ("┌----------------┐"    
        "|  ●             |"
        "|                |"
        "|                |"
        "|             ●  |"    
        "└----------------┘"),
    3: ("┌----------------┐"    
        "|  ●             |"
        "|       ●        |"
        "|                |"
        "|             ●  |"    
        "└----------------┘"),
    4: ("┌----------------┐"    
        "|  ●          ●  |"    
        "|                |"
        "|                |"
        "| ●           ●  |"        
        "└----------------┘"),
    5: ("┌----------------┐"    
        "|  ●          ●  |"    
        "|       ●        |"
        "|                |"
        "|  ●          ●  |"        
        "└----------------┘"
        ),
    6: ("┌----------------┐"    
        "|  ●          ●  |"        
        "|  ●          ●  |"
        "|                |"
        "|  ●          ●  |"        
        "└----------------┘"),
    }
dice = []
Total = 0
number_of_dice = int(input("How many dice would you like to roll?: "))
for die in range(number_of_dice):
    dice.append(random.randint(1, 6))
    
for die in range(number_of_dice):
    for line in dice_art.get(dice[die]):
            print(line)
        
            
for die in dice:
    Total += die
   
print(f"Total value of dice: {Total}")