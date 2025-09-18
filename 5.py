questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Who wrote the national anthem of India?",
        "options": ["A. Rabindranath Tagore", "B. Mahatma Gandhi", "C. Bankim Chandra Chatterjee", "D. Subhas Chandra Bose"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "How many players are there in a cricket team?",
        "options": ["A. 9", "B. 10", "C. 11", "D. 12"],
        "answer": "C"
    },
    {
        "question": "Which is the largest mammal on Earth?",
        "options": ["A. African Elephant", "B. Giraffe", "C. Blue Whale", "D. Polar Bear"],
        "answer": "C"
    }
]


prize_per_question = [1000, 2000, 5000, 10000, 20000]
total_prize = 0


print("🎉 Welcome to Kaun Banega Crorepati (KBC) 🎉\n")
input("Press Enter to start the game...")


for i, q in enumerate(questions):
    print(f"\nQuestion {i+1}: {q['question']}")
    for option in q["options"]:
        print(option)
    
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print("✅ Correct Answer!")
        total_prize += prize_per_question[i]
        print(f"You've won ₹{prize_per_question[i]}")
    else:
        print("❌ Wrong Answer!")
        print(f"The correct answer was: {q['answer']}")
        break  

print("\n💰 Game Over!")
print(f"Total Prize Money Won: ₹{total_prize}")