
# Explain 2 main ways that sets are different to lists and tuples
# - Uniqueness: Sets do not allow duplicate element.
# - Order: Sets are unordered collections.

# Create a set named 'fruits' containing "apple", "banana", and "cherry".
fruits = set(["apple","banana","cherry"])

# Print the set 'fruits'
print(fruits)

# Add "orange" to the fruits set using one of the set's methods.
fruits.add("orange")
# Print the set 'fruits' - check it's added
print(fruits)
# Remove "banana" from the fruits set using one of the set's methods.
fruits.remove("banana")
# Print the set 'fruits' - check it's removed
print(fruits)
# Attempt to add another "apple" to the fruits set. What do you observe? Why does this happen?
# - Elements can't be repeated in sets, they must be unique.
fruits.add("apple")
# Print the final fruits set.
print(fruits)
# Print the 2nd item in the set. If there is any problem doing this, explain.
# - Sets are undordered so their children are not indexed
print(list(fruits)[1])