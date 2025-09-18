numbers = [12, 7, 9, 20, 15, 8]


even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)


print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)