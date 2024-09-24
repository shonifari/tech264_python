
# ### How are tuples similar to lists?
# - **Structure**: Both tuples and lists are used to store collections of items.
# - **Indexing**: Both support indexing, slicing, and iteration.
# - **Heterogeneous**: Both can store items of different data types.
#
# ### Are tuples immutable and what does this mean?
# - **Yes, tuples are immutable**. This means that once a tuple is created, its elements cannot be changed, added, or removed. This immutability ensures that the data remains constant throughout the program.
#
# ### What other data types are immutable?
# - **Strings**
# - **Integers**
# - **Floats**
# - **Booleans**
# - **Frozensets**
#
# ### What is a good use case for tuples?
# - **Fixed Data**: Tuples are ideal for storing fixed collections of items, such as coordinates (x, y), RGB color values, or any data that should not change throughout the program.
#
# ### What does the following piece of code do?
# Please provide the code snippet you want to analyze, and I'll explain what it does!

essentials = ("bread", "eggs", "milk")

print(essentials)

print(essentials.count("bread"))

# "Stranded on a Desert Island" game

# Rationale: Practice tuples

# Type of exercise: Finish the code

print("You are stranded on a desert island. You can take only THREE items.")

essential_item1 = input("What is an essential item you would take? ")

essential_item2 = input("What is an essential item you would take? ")

essential_item3 = input("What is an essential item you would take? ")

# save the items as a tuple

essentials_tuple = (essential_item1,essential_item2, essential_item3)

# print the tuple

print("Here are your items as a tuple:", essentials_tuple)

print("")

print("I lied. You can take one more item.")

essential_item4 = input("What is one more essential item you would take? ")

# try to add the 4th item to the tuple

# if you can't add the 4th item, work out how to save the 4th item to the tuple

essentials_tuple = essentials_tuple + (essential_item4,)

print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)

