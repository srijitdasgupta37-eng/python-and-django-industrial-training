import random


moves = ["rock", "paper", "scissors"]

def decide_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"


def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("🎮 Welcome to Rock-Paper-Scissors!")
    print("Type 'exit' to quit the game.\n")

    while True:
        print(f"\nRound {round_number}:")
        user_move = input("Enter your move (rock/paper/scissors): ").lower()

        if user_move == "exit":
            break
        if user_move not in moves:
            print("❌ Invalid move. Try again.")
            continue

        computer_move = random.choice(moves)
        print(f"Computer chose: {computer_move}")

        winner = decide_winner(user_move, computer_move)

        if winner == "draw":
            print("It's a draw!")
        elif winner == "user":
            print("✅ You win this round!")
            user_score += 1
        else:
            print("💻 Computer wins this round!")
            computer_score += 1

        round_number += 1

    
    print("\n🏁 Game Over!")
    print(f"Final Score - You: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print("🎉 Congratulations! You won the game!")
    elif user_score < computer_score:
        print("😞 Better luck next time. Computer wins.")
    else:
        print("🤝 It's a tie!")


play_game()