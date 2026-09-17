text = "programming"

result = ""

for char in text:
    if char not in result:
        result += char

print("Original string:", text)
print("String without duplicates:", result)
