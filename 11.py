scores = [95, 82, 67, 45, 77]


try:
    user_score = int(input("Enter a score: "))

    
    if user_score in scores:
        
        if user_score >= 90:
            grade = "A"
        elif 75 <= user_score <= 89:
            grade = "B"
        elif 60 <= user_score <= 74:
            grade = "C"
        else:
            grade = "F"
        
        print(f"The grade for score {user_score} is: {grade}")
    else:
        
        print("Score not found")

except ValueError:
    print("Invalid input. Please enter a valid integer score.")