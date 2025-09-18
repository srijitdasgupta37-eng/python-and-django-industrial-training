ages = [16, 18, 20, 15, 21, 17]


for age in ages:
    if age == 21:
        print("Access granted")
        print("VIP customer detected. Stopping check.")
        break  
    elif age >= 18:
        print("Access granted")