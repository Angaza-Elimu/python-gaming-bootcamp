print("🔢 AWESOME CALCULATOR")
print("=" * 40)

# Get the first number from the user
num1 = float(input("Enter first number: "))

# Display the menu of operations
print("\nChoose an operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (×)")
print("4. Divide (÷)")
print("5. Power (^)")

# Get the operation choice
operation = input("\nEnter operation number (1-5): ")

# Get the second number
num2 = float(input("Enter second number: "))

# Perform the calculation based on user's choice
print("\n" + "=" * 40)
print("CALCULATING...")
print("=" * 40 + "\n")

if operation == "1":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "2":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "3":
    result = num1 * num2
    print(f"{num1} × {num2} = {result}")
elif operation == "4":
    # Check for division by zero
    if num2 == 0:
        print("❌ Error! Cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"{num1} ÷ {num2} = {result}")
elif operation == "5":
    result = num1 ** num2
    print(f"{num1} ^ {num2} = {result}")
else:
    print("❌ Invalid operation!")

print("\n✅ Thanks for using the calculator!")