user_input = input("Enter a string: ")

normalized = user_input.replace(" ", "").lower()

if normalized == normalized[::-1]:
    print("The string is a palindrome.")
else:

    transformed = user_input + user_input[::-1]
    print("The string is not a palindrome.")
    print("Transformed palindrome:", transformed)