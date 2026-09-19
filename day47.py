numbers = [10, 25, 7, 45, 30, 15]

smallest = numbers[0]
largest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

    if num > largest:
        largest = num

difference = largest - smallest

print("Smallest number:", smallest)
print("Largest number:", largest)
print("Maximum difference:", difference)
