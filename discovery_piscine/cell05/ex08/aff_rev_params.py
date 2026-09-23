import sys

param_count = len(sys.argv) - 1
if param_count >= 2:
    for param in reversed(sys.argv):
        print(param)
else:
    print("none")