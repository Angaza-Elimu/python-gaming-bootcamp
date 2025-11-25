# Step 1: Get a number from the user and convert it to an integer
x = int(input("Please input a number: "))

# Step 2: Check if the number is even or odd
if x % 2 == 0:  # If remainder is 0 when divided by 2, the number is even
    print('x is even')
else:
    print('x is odd')