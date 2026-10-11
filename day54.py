numbers = (10, 20, 30, 40, 50)

print("Original tuple:", numbers)

# Convert tuple into a list
number_list = list(numbers)

# Modify the list
number_list.append(60)
number_list[0] = 5

# Convert back into a tuple
numbers = tuple(number_list)

print("Updated tuple:", numbers)
