first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
result = first_number*second_number
print(f"{first_number} x {second_number} = {result}")
print("This number is positive." if result > 0 else "This number is negative." if result < 0 else "This number is both positive and negative.")