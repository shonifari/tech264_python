# Rationale
#
# Practice control flow
# Practice completing user stories
#
#
#
# Task
#
# Level 1
#
# Challenge yourself to get Level 1 done in 15 min
# Comments in the code are to help you meet user requirements, but you may need to write code in the order you think is necessary
# ```
#
# # User story 1
#
# # As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.



# Define/assign number to a variable called magic_number

magic_number = 3
#
#
#
#
#
guesses = 1
while guesses <= 5:
    # Ask user for input
    user_guess = input("Take a guess at the magic number?: ")

    # Check if this input matches magic_number
    if user_guess.isdigit() and int(user_guess) == magic_number:
        print(f"Congratulations! Your guess was correct. The magic number is {magic_number}")
        break
    else:
        print(f"Unfortunate! Try again, you still have {5 - guesses} guesses left.")
    guesses += 1




#
# Level 2
#
# Challenge yourself to get from Level 1 to Level 2 in 10 min
#
# ```
#
# # User story 2
#
# # As a user, I want to be able to guess a number and know if I need to go higher or lower.
#
guesses = 1
while guesses <= 5:
    # Ask user for input
    user_guess = input("Take a guess at the magic number?: ")
    if not user_guess.isdigit():
        print("Magic number must be a number")
        continue

    user_guess = int(user_guess)

    # Check if this input matches magic_number
    if user_guess == magic_number:
        print(f"Congratulations! Your guess was correct. The magic number is {magic_number}")
        break


    print(f"Unfortunate! Your guess was {'too low' if guesses < magic_number else 'too high'}\nTry again, you still have {5 - guesses} guesses left.")

    guesses += 1



# # User story 3
#
# # As a user, I don't want my guesses wasted if I enter something accidently as my guess which are not digits.

guesses = 1
while guesses <= 5:
    # Ask user for input
    user_guess = input("Take a guess at the magic number?: ")
    if not user_guess.isdigit():
        print("Magic number must be a number")
        continue

    user_guess = int(user_guess)

    # Check if this input matches magic_number
    if user_guess == magic_number:
        print(f"Congratulations! Your guess was correct. The magic number is {magic_number}")
        break


    print(f"Unfortunate! Your guess was {'too low' if guesses < magic_number else 'too high'}\nTry again, you still have {5 - guesses} guesses left.")

    guesses += 1

#
#
# # User story 4
#
# # As a user, after each guess, I would like to know how many guesses I have left.

guesses = 1
while guesses <= 5:
    # Ask user for input
    user_guess = input("Take a guess at the magic number?: ")
    if not user_guess.isdigit():
        print("Magic number must be a number")
        continue

    user_guess = int(user_guess)

    # Check if this input matches magic_number
    if user_guess == magic_number:
        print(f"Congratulations! Your guess was correct. The magic number is {magic_number}")
        break


    print(f"Unfortunate! Your guess was {'too low' if guesses < magic_number else 'too high'}\nTry again, you still have {5 - guesses} guesses left.")

    guesses += 1


# Level 3
#
# Challenge yourself to get from Level 2 to Level 3 in 10 min
#
# ```
#
# # User story 5
#
# # As a user, I would like the magic to be randomly generated each time I play so it is more fun.
#

import random

magic_number = random.randint(1,10)
guesses = 1
while guesses <= 5:
    # Ask user for input
    user_guess = input("Take a guess at the magic number?: ")
    if not user_guess.isdigit():
        print("Magic number must be a number")
        continue

    user_guess = int(user_guess)

    # Check if this input matches magic_number
    if user_guess == magic_number:
        print(f"Congratulations! Your guess was correct. The magic number is {magic_number}")
        break


    print(f"Unfortunate! Your guess was {'too low' if guesses < magic_number else 'too high'}\nTry again, you still have {5 - guesses} guesses left.")

    guesses += 1

# # User story 6
#
# # As a user, I would like to know the magic number at the end of the game if I still haven't guessed correctly and I've used up all my tries.

import random

magic_number = random.randint(1,10)
guesses = 1
while guesses <= 5:
    # Ask user for input
    user_guess = input("Take a guess at the magic number?: ")
    if not user_guess.isdigit():
        print("Magic number must be a number")
        continue

    user_guess = int(user_guess)

    # Check if this input matches magic_number
    if user_guess == magic_number:
        print(f"Congratulations! Your guess was correct. The magic number is {magic_number}")
        break


    print(f"Unfortunate! Your guess was {'too low' if guesses < magic_number else 'too high'}\nTry again, you still have {5 - guesses} guesses left.")

    if guesses == 5:
        print(f"GAME OVER! You have finished your attempts. The magic number was {magic_number}")
    else:
        guesses += 1

# Hint:
#
# Use the Python library random to generate a random number rather than assigning one
#