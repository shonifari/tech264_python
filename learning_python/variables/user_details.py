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


# Use your code from the "Task: Get name, age and DOB details from a user".
# Mix the name, age and DOB into one list user_details_list
# Print the user's name, age and DOB from the list
user_details_list = [name, age , dob]
print(user_details_list[0])
print(user_details_list[1])
print(user_details_list[2])

# Check the age is saved as an integer in the list. If it's not, work out how to convert it to an integer and add the age integer to the list.
if type(user_details_list[1]) != int:
    user_details_list[1] = int(user_details_list[1])

# Ask the user for their height in cm and save it to the variable height
height = input("What's your height in cm?: ")

# Save height as a float in the list, and print the height from the list.
user_details_list.append(float(height))

