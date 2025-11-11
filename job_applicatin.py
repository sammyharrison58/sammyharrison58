Name =input("please enter you name :")
if len (Name)>12:
    print("Not more than 12 ")
elif not Name.find(" ") == -1:
    print("username must not contain spaces.")
elif not Name.isalpha():
    print("Your username cant contain numbers ")
else:
    print("welcome to Noblesse company")
print(f"Welcome to the system {Name} ")
job=input("do you want to apply for a job(yes/no) ?")
if job.lower() =="yes":
    print("Here is a list of avaailable vacant jobs")
    print("a) lab tech")
    print("b) Graphic desighner")
    print("c) website desighner")
    print("d) backend developer")
application = input("please enter the letter of the job u want to apply for? ")
if application.lower() in ['a','b','c','d']:
    print("we would like you to attach your CV,any other certificates at the bottom")
    print("we would like you to enter the required details below")
experience=input("do you have any experience in the job you are appliying for?(yes/no)")
if experience.lower()=="yes":
    input("How many years ? ")
    input("which organization ? ")
    input("why do you think we should employ you for the post  ? ")
    input("what other skills do you have except the required ones ? ")
    print("Thank you for the infomation above")
    #Now lets validate the informatio above
    input("Name your Recomendee?(should be valid) ")
    input("What the main reason why you applied for the job?" )
    input("Are u employed?(yes/no) if yes where")
    input("If you were given this job which changes would You bring? ")
    print("Thank you {Name} for your time,You will be contacted on the results")
    print("\n🧾 Your experience:")
print("we do applologize but we need experienced applicants for these post")



