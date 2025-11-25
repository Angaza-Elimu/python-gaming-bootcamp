import random

print("✊ ROCK PAPER SCISSORS ✋")
print("=" * 40)

# Initialize scores
player_score = 0
computer_score = 0
rounds = 0

while True:
    print(f"\n🎮 Round {rounds + 1}")
    print(f"Score - You: {player_score} | Computer: {computer_score}")
    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")
    
    choice = input("\nYour choice (1-4): ")
    
    # Check if player wants to quit
    if choice == "4":
        print("\n👋 Thanks for playing!")
        break
    
    # Validate input
    if choice not in ["1", "2", "3"]:
        print("❌ Invalid choice!")
        continue
    
    # Convert choice to name
    choices = ["Rock", "Paper", "Scissors"]
    player = choices[int(choice) - 1]
    computer = random.choice(choices)
    
    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")
    
    # Determine winner
    if player == computer:
        print("🤝 It's a tie!")
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        print("🎉 You win this round!")
        player_score += 1
    else:
        print("💻 Computer wins this round!")
        computer_score += 1
    
    rounds += 1

# Display final results
print("\n" + "=" * 40)
print("FINAL SCORE")
print("=" * 40)
print(f"You: {player_score}")
print(f"Computer: {computer_score}")

if player_score > computer_score:
    print("\n🏆 YOU WIN!")
elif player_score < computer_score:
    print("\n😢 Computer wins!")
else:
    print("\n🤝 It's a tie overall!")