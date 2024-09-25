# Summary
#
# Print incremented numbers to the screen but substitute multiples of 3 with 'Fizz', multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'
#

#
# The task
#
# Core:
#
# Make a new 'fizzbuzz.py' file
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz" instead of the number
# For numbers which are multiples of both three and five print "FizzBuzz".

def fizzbuzz(fizz = 3, buzz = 5):
    for i in range(1,101):
        if i%fizz == 0 and i%buzz == 0:
            print("FizzBuzz")
        elif i%fizz == 0:
            print("Fizz")
        elif i%buzz == 0:
            print("Buzz")
        else:
            print(i)



fizzbuzz(3,5)

# If time:
#
# Improve the script so we can decide which numbers to substitute for "Fizz" and "Buzz"
# Refactor using functions

fizzbuzz(10,10)
# Acceptance Criteria
#
# All core task are done
# Core works with no error
#