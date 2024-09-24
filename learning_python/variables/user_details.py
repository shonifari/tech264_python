# Write a Python script to:
# •	Get the user's name, age and DOB.
# •	Print the user's name, age and DOB to the screen
# If time, see if you can:
# •	prompt the user and get the input on the same line
# •	see if you can print "Hi " on the one line


name = input("What's your name?: ")
age = input("What's your age?: ")
dob = input("What's your date of birth?: ")

print(f"Hi {name}")
print(f"You were born on {dob}, therefore your age is {age}")