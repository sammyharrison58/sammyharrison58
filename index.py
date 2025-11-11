#Displaying a message
print("good work")
password="secret word"
password = 1234
# Asking for a password until the correct one is entered
print("Enter the password:")
Guess = input ()
while Guess != password:
    Guess = input("Incorrect password, try again: ")    
guess = input()
if guess == password:
    print("Access granted")
else:
    print("Access denied")      
# Displaying a message
print("You have successfully logged in")    
# Displaying a message
print("Welcome to the system")  