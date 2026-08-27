marks = {
    "Maths": 85,
    "Python": 90,
    "English": 78,
    "AI": 88
}

total = 0

for subject, mark in marks.items():
    total += mark

average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)
