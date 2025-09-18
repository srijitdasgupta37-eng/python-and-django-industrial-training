total_sum = 0

print("Enter numbers to add to the sum.")
print("Enter 0 to stop. Negative numbers will be ignored.\n")

while True:
    try:
        num = int(input("Enter a number: "))
        
        if num == 0:
            break  
        elif num < 0:
            print("Negative number ignored.")
            continue  
        else:
            total_sum += num  

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


print(f"\nTotal sum of valid positive numbers: {total_sum}")