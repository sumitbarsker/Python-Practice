marks = [78, 85, 92, 67, 88, 74, 95]

total = 0
highest = marks[0]
lowest = marks[0]

for mark in marks:
    total += mark

    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
