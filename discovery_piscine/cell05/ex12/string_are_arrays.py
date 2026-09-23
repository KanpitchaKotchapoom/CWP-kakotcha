import sys

if len(sys.argv) == 2:
    word = sys.argv[1]
    count = word.count("z")

    if count > 0:
        print("z" * count)
    else:
        print("none")
else:
    print("none")