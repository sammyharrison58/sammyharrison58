principal=0
rate=0
time=0
while principal<=0:
    principal=float(input("Enter the principal amount: "))
    if principal<=0:
        print("Principal must be greater than 0.")
while rate<=0:
    rate=float(input("Enter the rate of interest: "))
    if rate<=0:
        print("Rate must be greater than 0.")
while time<=0:
    time=int(input("Enter the time in years: "))
    if time<=0:
        print("Time must be greater than 0.")
simple_interest=principal*pow((1+rate/100),time)
print(f"balance after {time} years is:$ {simple_interest:.2f}")