# AND - Both conditions must be True for the result to be True
age = 16
has_license = True

if age >= 16 and has_license:
    print("You can drive!")
else:
    print("You cannot drive yet.")

# OR - At least one condition must be True for the result to be True
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No school today!")
else:
    print("Time for class.")

# NOT - Reverses the Boolean value (True becomes False, False becomes True)
is_raining = False

if not is_raining:
    print("Great day for a walk!")
else:
    print("Bring an umbrella.")


