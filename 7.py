students = ["Alice", "Bob", "Charlie", "David", "Eva"]


for i in range(3):
    name = input(f"Enter student name ({i+1}/3): ")

    
    if name in students:
        print(f"Student {name} is enrolled.")
    else:
        print(f"Student {name} is not found.")