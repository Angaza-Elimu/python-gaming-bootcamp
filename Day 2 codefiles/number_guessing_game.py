# Guess the secret number
secret_number = 7
guess = 0

print("I'm thinking of a number between 1 and 10")

while guess != secret_number:
    guess = int(input("Your guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 You got it!")