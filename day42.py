numbers = [10, 20, 10, 30, 40, 20, 50, 10]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate elements:", duplicates)
