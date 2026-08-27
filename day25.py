numbers = [10, 20, 10, 30, 20, 10, 40, 20, 20]

most_frequent = numbers[0]
max_count = 0

for num in numbers:
    count = 0

    for item in numbers:
        if item == num:
            count += 1

    if count > max_count:
        max_count = count
        most_frequent = num

print("Most frequent number:", most_frequent)
print("Frequency:", max_count)
