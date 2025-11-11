name=input("Enter your name: ")
if len(name)<12:
    print("Name must be at least 12 characters long")
else:
    print("Welcome",name)
age=int(input("Enter your age: "))
if age<18:
    print("You must be at least 18 years old to proceed")
else:
    print("You are eligible to proceed")