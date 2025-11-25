print("🤖 PERSONALIZED GREETING BOT")
print("=" * 40)

# Get user information
name = input("What's your name? ")
age = int(input("How old are you? "))
hobby = input("What's your favorite hobby? ")

# Create a personalized message
print("\n✨ GENERATING YOUR PROFILE... ✨")
print(f"\nHey {name}! Welcome to Python coding!")
print(f"At {age} years old, you're the perfect age to learn programming.")
print(f"Fun fact: Many famous programmers started around your age!")
print(f"Since you enjoy {hobby}, you could build apps related to that!")

# Calculate approximate birth year
current_year = 2025
birth_year = current_year - age
print(f"\nYou were probably born in {birth_year}.")

# Motivational ending
print("\n💪 Keep coding and you'll build amazing things!")