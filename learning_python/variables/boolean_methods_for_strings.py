hi = "Hello World!"

# Find out if 'hi' is made up of letters only (use one of the string methods)
print(hi.isalpha())  # False, because there is a space and punctuation in the string

# Find out if 'hi' is made up only of lowercase letters
print(hi.islower())  # False, because it has uppercase letters and punctuation

# Find out if 'hi' is made up only of uppercase letters
print(hi.isupper())  # False, it has both uppercase and lowercase letters

# Find out if 'hi' ends with an exclamation mark
print(hi.endswith("!"))  # True, it ends with an exclamation mark

# Find out if 'hi' starts with a capital "H"
print(hi.startswith("H"))  # True, it starts with "H"
