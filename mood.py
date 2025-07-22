# asking a question
def ask_question():
    question = input("how are you feeling today?")          
    print(f"You asked: {question}")
input ()
answer = input()
print ("please enter your mood")
if answer.lower() == "happy":
    print("That's great to hear! Keep smiling!")    
elif answer.lower() == "sad":
    print("I'm sorry to hear that. I hope things get better soon.")     
elif answer.lower() == "angry":
    print("It's okay to feel angry sometimes. Take a deep breath and try to relax.")    
elif answer.lower() == "excited":
    print("Wow! That's awesome! Enjoy the excitement!")     
elif answer.lower() == "bored":
    print("Maybe try something new to shake things up a bit!")
else:
    print("thats an interesting mood! Tell me more about it.")
    