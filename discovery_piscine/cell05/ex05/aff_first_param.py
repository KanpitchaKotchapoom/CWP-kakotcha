import sys

param_count = len(sys.argv) - 1
if param_count == 0:
    print("none")
else:
    print(sys.argv[1])