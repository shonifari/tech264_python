# Objective
#
# Understand the concept and usage of immutable sets (frozen sets).
#
# Create a frozen set named frozen_set containing elements "hello", "world".
forzen_set = frozenset(["hello", "world"])
print(forzen_set)

# Try to add "!" to frozen_set. What happens?
try:
    frozenset.add("!")
except Exception as e:
    print(f"Error: {e}")

# Create a normal set named normal_set containing elements "let's", "learn".
normal_set = set(["let's","learn"])
# Try to add frozen_set to normal_set. Why does it work? Explain.
normal_set.add(forzen_set)

# Print normal_set.
print(normal_set)

# Run your script half a dozen times.
# What do you notice about where frozen_set is added to normal_set? Hint: Look at the order of the items.

# What makes a frozen set different to a normal set? Explain.