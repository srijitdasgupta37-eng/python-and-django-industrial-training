def is_rotation(s1, s2):

    if len(s1) != len(s2):
        return False

    return s2 in (s1 + s1)

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if is_rotation(str1, str2):
    print("Yes, the second string is a rotation of the first.")
else:
    print("No, the second string is NOT a rotation of the first.")