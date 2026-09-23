og_arr = [1, 9, 25, 47, 9, 91, -11, 25]
new_arr = set()
for i in og_arr:
    if i > 5:
        i += 2
        new_arr.add(i)
print(og_arr)
print(new_arr)