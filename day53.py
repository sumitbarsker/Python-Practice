numbers = (10, 20, 10, 30, 20, 10, 40)

target = 10
count = 0

for num in numbers:
    if num == target:
        count += 1

print("Tuple:", numbers)
print("Element:", target)
print("Frequency:", count)
