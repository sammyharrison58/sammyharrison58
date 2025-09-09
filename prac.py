username = input("Enter username: ")
if len(username) < 12:
    print("username must be at least 12 characters long.")
elif not username.find(" ") == -1:
    print("username must not contain spaces.")
elif not username.isalpha():
    print("Your username cant contain numbers ")
else:
    print(f"welcome {username }")  
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
vote = input("Do you want to vote? (yes/no): ")
if vote.lower() == "yes":
    print("Here are the candidates for presidency:")
    print("a) Alice")
    print("b) Bob")
    print("c) Charlie")
    print("d) Diana")
presidency = input("Please enter the name of the candidate you want to vote for: ")
other_officials=input("would u like to vote for othe government officials? (yes/no) ")
if other_officials.lower() == "yes":
    print("Here are the seats for other government officials:")
    print("a) prime minister")
    print("b) vice president")
    print("c) mayor")
    print("d) governor")
Seating = input("please enter the letter of the official u want to elect: ")
if Seating.lower() in ['a']:
    print("Here are the candidates for prime minister:")
    print("1) John")
    print("2) son") 
prime_minister=input("please enter the name of the candidate you want to vote for: ")
if Seating.lower() in ['b']:
    print("Here are the candidates for vice president:")
    print("1) Mike")
    print("2) Ike")
vice_president=input("please enter the name of the candidate you want to vote for: ")
if Seating.lower() in ['c']:
    print("Here are the candidates for mayor:")
    print("1) Sarah")
    print("2) Lara")
mayor=input("please enter the name of the candidate you want to vote for: ")
if Seating.lower() in ['d']:  
    print("Here are the candidates for governor:")
    print("1) Tom")
    print("2) Jerry")
governor=input("please enter the name of the candidate you want to vote for: ")
print("Thank you for voting!")


