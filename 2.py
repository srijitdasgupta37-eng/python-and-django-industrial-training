text = input("Enter a string: ")

while "  " in text:
    text = text.replace("  ", " ")

print("Updated string:", text)