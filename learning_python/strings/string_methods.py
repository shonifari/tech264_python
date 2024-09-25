

str_with_extra_spaces = "   extra spaces at the start and end   "

# Write comment to explain what this does
# Prints the sum of the character in the string
print(len(str_with_extra_spaces))

# Write comment to explain what this does
print(len(str_with_extra_spaces.strip()))


example_text = "here's some text with some words of text"

# Count how many times the substring 'text' occurs within example_text & print it to the screen
count_text = example_text.count('text')
print(f"The substring 'text' occurs {count_text} times.")

# Convert example_text to lowercase & print it to the screen
lowercase_text = example_text.lower()
print(f"Lowercase: {lowercase_text}")

# Convert example_text to uppercase & print it to the screen
uppercase_text = example_text.upper()
print(f"Uppercase: {uppercase_text}")

# Capitalize the first letter in example_text & print it to the screen
capitalized_text = example_text.capitalize()
print(f"Capitalized: {capitalized_text}")

# Replace the word 'with' in example_text with a comma (,) instead & print it to the screen
replaced_text = example_text.replace(' with', ',')
print(f"Replaced: {replaced_text}")
