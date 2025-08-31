username = input("Enter username: ")
if len(username) < 12:
    print("username must be at least 12 characters long.")
elif not username.find(" ") == -1:
    print("username must not contain spaces.")
elif not username.isalpha():
    print("Your username cant contain numbers ")
else:
    print(f"welcome {username }")