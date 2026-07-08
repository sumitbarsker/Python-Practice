numbers = [12, 45, 7, 89, 34, 56]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("The smallest number is:", smallest)
