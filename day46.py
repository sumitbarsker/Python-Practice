numbers = [1, 2, 3, 5, 6, 7]

n = 7

expected_sum = n * (n + 1) // 2

actual_sum = 0

for num in numbers:
    actual_sum += num

missing_number = expected_sum - actual_sum

print("Missing number:", missing_number)
