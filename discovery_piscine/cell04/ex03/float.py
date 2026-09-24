text = input("Give me a number: ")
print("This number is an integer." if text.isdecimal() or float(text).is_integer() else "This number is a decimal.")