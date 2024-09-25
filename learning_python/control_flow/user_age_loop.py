# Make a new file named prompt_user_for_age_loop.py or similar.
#
# 1. Loop until age is all digits
#
# Look at this code:
#
# ```
#
# # Ask user for their age
#
# age = input("What is your age? ")
#
#
#
# print(f" Your age is {age}")
#
# ```
#
# The problem with this code is that even if the user is 20, they could enter "20" or "twenty". Let's standardise the input to get the age as digits...
#
# Starting code - replace comments in CAPITALS with your code:
#
# ```



# user_prompt = True
# age = None
# while user_prompt:
#     age = input("What is your age? ")
#     if age.isdigit():
#         user_prompt = False
#     else:
#         print(f"Error! age needs to be a whole number. It can't be: {age}")
#
# print(f"Your age is {age}")
#



# 2. Also check age is in the correct range
#
# Our code now works to stop our user from inputting strings, floats, and negative numbers, but at the moment the user could say they are 356000 years old if they want.
#
# Assuming the oldest person alive today is 117, modify your code to only allow a maximum of 117 as the age.
#
user_prompt = True
age = None
while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print(f"Error! Age needs to be a whole number and below 117. It can't be: {age}")

print(f"Your age is {age}")

