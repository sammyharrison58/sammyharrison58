# asking a question
def ask_question():
    question = input("What is your question? ")
    print(f"You asked: {question}")
print("good work") 
# displaying a message
print("Welcome to the number guessing game!")
# askining a quiz
def i_am_thinking_of_a_number_between_1_and_100():
    import random
    number = random.randint(1, 100)
    guess = input()
    while guess != number:
        guess = int(input())
        if guess < number:
            print("Too low!")
            guess = int(input())
        elif guess > number:
            print("Too high!")
            guess = int(input())
        else:
            print("Congratulations! You guessed it right.") 
# asking for number until the correct one is entered
print("Enter a number between 1 and 100:")
guess = int(input())
import random
number = random.randint(1, 100)
while guess != number:
    if guess < number:
        print("Too low! Try again.")                
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right.")
    guess = int(input("Enter a number between 1 and 100: "))
    print("Congratulations! You guessed it right.")
       
    
