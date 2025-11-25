# Login system - user gets 3 attempts
password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter password: ")
    attempts = attempts + 1
    
    if user_input == password:
        print("✅ Access granted!")
        break  # Exit the loop immediately
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"❌ Wrong password. {remaining} attempts left.")
        else:
            print("❌ Account locked!")