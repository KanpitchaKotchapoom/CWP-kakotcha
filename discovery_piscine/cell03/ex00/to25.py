goal = 25
starter = int(input("Enter a number less than 25\n"))
if starter < goal:
    while starter <= goal:
        print(f"Inside the loop, my variable is {starter}")
        starter += 1
else:
    print("Error")