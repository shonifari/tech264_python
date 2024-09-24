# What's a variable?
#
# - A variable is a value that we assign in the program and gets stored in memory for future use.
#
#
# Why is it called a variable?
#
# - A variable is called like that because it's value can be changed in our program after it has been assigned.
#
#

# Set a variable to a number value
number = 1

# Set a variable to a decimal
decimal = .0

# Set a variable to a string value
string = "string"


# How is using '==' different?
#- '=' is the assignment operator while '==' is the is equal operator that checks if left is equal to right.

# Print the data type of your variables
print(type(number))
print(type(decimal))
print(type(string))


# Overwrite the value of a previous number with a new number

print(id(number))
number = 2
print(id(number))

# Why the ID of the variable changes?
# Becuase integer are immutable therefore when we modify it it will return a different memory address.


# Ask the user for some input and print the input to the screen
print ((1))
name = input("WHats your name?: ")
print(f'Hello {name}')
