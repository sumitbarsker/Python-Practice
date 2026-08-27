def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


number = 25

result = check_even_odd(number)

print(number, "is", result)
