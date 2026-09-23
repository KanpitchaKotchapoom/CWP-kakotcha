import sys

param_count = len(sys.argv) - 1
if param_count == 1:
    print(sys.argv[1].upper())
else:
    print("none")