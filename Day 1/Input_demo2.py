# This code will cause an error!
age = input("Enter your age: ")
next_year = age + 1  # ERROR! Cannot add a number to text

# CORRECT: Convert the input to an integer first
age = int(input("Enter your age: "))
next_year = age + 1
print("Next year you'll be", next_year)