import math
# This file is part of the Noblesse project.
#python calculator
operator = input("Enter operator (+, -, *, /, ^, sqrt): ")
print("Enter numbers (separated by space):")
input_numbers = input().split()
numbers = [float(num) for num in input_numbers]
result = None
if operator == '+':
    result = sum(numbers)
elif operator == '-':
    result = numbers[0]
    for num in numbers[1:]:
        result -= num   
elif operator == '*':
    result = 1
    for num in numbers:
        result *= num   
elif operator == '/':
    result = numbers[0]
    for num in numbers[1:]:
        if num != 0:
            result /= num
        else:
            print("Error: Division by zero")
            result = None
            break       
elif operator == '^':
    result = numbers[0] ** numbers[1] if len(numbers) > 1 else None
elif operator == 'sqrt':
    if len(numbers) == 1:
        result = math.sqrt(numbers[0])
    else:
        print("Error: Square root requires one number")
if result is not None:
    print(f"Result: {result}")
# This file is part of the Noblesse project.

        
    
    
    

    
