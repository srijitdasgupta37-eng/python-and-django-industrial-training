words = ["Python", "is", "an", "amazing", "language"]


n = int(input("Enter a number (n): "))


print(f"Words with length greater than {n}:")
for word in words:
    if len(word) > n:
        print(word)