list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

combined = []

for num in list1:
    if num not in combined:
        combined.append(num)

for num in list2:
    if num not in combined:
        combined.append(num)

print("Combined list:", combined)
