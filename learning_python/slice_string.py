# Explain: What is slicing strings?
# to return a part of the string


Hw = "Hello world!"

print(Hw)

# Find out how many characters Hw has

print(len(Hw))
# Get the character in the first position in Hw

Hw[0]
# Get the last character

Hw[-1]
# Get the 2nd last character

Hw[-2]
# Write a comment to EXPLAIN what does this do
# This returns the string except the first 3 characters
print(Hw[2:])

# Write a comment to EXPLAIN what does this do
# This creates the only last 3 charachters
print(Hw[-3:])

# Write a comment to EXPLAIN what does this do
# This prints the first 5 ch
print(Hw[:5])

# Starts from the second, stops at the fifth (doesn't include it)

