import sys

if len(sys.argv) == 2:
    correct = sys.argv[1]
    
    check = input("What was the parameter? ")
    if check == correct:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")