name=input("enter ur full name:")
if len(name)<15:
    print("name must be at least 15 characters")
else:
    print("name is valid")
reg_no=input("enter ur registration number:")
if len(reg_no)!=8 or not reg_no[:2].isalpha() or not reg_no[2:6].isdigit() or not reg_no[6:].isalpha():
    print("registration number must be in the format: 2 letters, 4 digits, 2 letters")
else:
    print("registration number is valid")
email=input("enter ur email address:")
registered_domain="@university.edu"
if not email.endswith(registered_domain):
    print(f"email must end with {registered_domain}")   
else:
    print("email is valid")
#describing the exam
print("The exam will consist of 10 multiple-choice questions.")
print("You will have 1 hour to complete the exam.")
print("Each question is worth 10 points.")
print("To pass the exam, you need to score at least 60 points.")
print("Good luck!")
#the exam
quiz1=input("What is the capital of France? a) Paris b) London c) Berlin d) Madrid:")
if quiz1.lower()=='a':
    print("correct")    
else:
    print("incorrect")
quiz2=input("What is 2 + 2? a) 3 b) 4 c) 5 d) 6:")
if quiz2.lower()=='b':
    print("correct")
else:
    print("incorrect")
quiz3=input("What is the largest planet in our solar system? a) Earth b) Mars c) Jupiter d) Saturn:")
if quiz3.lower()=='c':
    print("correct")
else:
    print("incorrect")
quiz4=input("What is the chemical symbol for water? a) CO2 b) H2O c) O2 d) NaCl:")
if quiz4.lower()=='b':
    print("correct")    
else:
    print("incorrect")
quiz5=input("Who wrote 'Romeo and Juliet'? a) Charles Dickens b) Mark Twain c) William Shakespeare d) Jane Austen:")
if quiz5.lower()=='c':
    print("correct")
else:
    print("incorrect")
quiz6=input("What is the smallest prime number? a) 0 b) 1 c) 2 d) 3:")
if quiz6.lower()=='c':
    print("correct")
else:
    print("incorrect")
quiz7=input("What is the boiling point of water at sea level? a) 90°C b) 100°C c) 110°C d) 120°C:")
if quiz7.lower()=='b':
    print("correct")
else:
    print("incorrect")
quiz8=input("Who painted the Mona Lisa? a) Vincent van Gogh b) Pablo Picasso c) Leonardo da Vinci d) Claude Monet:")
if quiz8.lower()=='c':
    print("correct")    
else:
    print("incorrect")
quiz9=input("What is the largest mammal in the world? a) Elephant b) Blue Whale c) Giraffe d) Great White Shark:")
if quiz9.lower()=='b':
    print("correct")
else:
    print("incorrect")
quiz10=input("What is the hardest natural substance on Earth? a) Gold b) Iron c) Diamond d) Silver:")
if quiz10.lower()=='c':     
    print("correct")
else:
    print("incorrect")
#validating user inputs
score2=count=0
answers=[quiz1,quiz2,quiz3,quiz4,quiz5,quiz6,quiz7,quiz8,quiz9,quiz10]  
correct_answers=['a','b','c','b','c','c','b','c','b','c']
for answer in answers:
    if answer.lower() in correct_answers:
        count+=1        
        score2=count*10
print(f"your score is {score2} out of 100")

score=int(input("enter your score to get your grade:"))
if score<0 or score>100:
    print("score must be between 0 and 100")
elif score<40:
    print("u got an E")
elif score>=40 and score<50:
    print("u got a D")
elif score>=50 and score<60:
    print("u got a C")
elif score>=60 and score<70:
    print("u got a B")
elif score>70:
    print("u got an A")
elif score==100:
    print("u got an A+")
elif score>100:
    print("invalid score")
welcome_msg="welcome to the exam portal"
print(welcome_msg.center(50,"*"))