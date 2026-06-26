text = "Python Programming"

count = 0

for char in text:
    if char != " ":
        count += 1

print("Total characters (without spaces):", count)
