years = [10, 20, 30]
present = int(input("Please tell me your age: "))
print(f"You are currently {present} years old")
for i in years:
    print(f"In {i} years, you'll be {present+i} years old.")