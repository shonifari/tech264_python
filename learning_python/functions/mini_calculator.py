# Recommended: Make a 'functions' folder inside your PyCharm project for storing learning about functions.
#
# Create a Python file called calculator.py and complete a viable basic calculator using functions.
#
# MVP (each of these should be in a separate function):
#
# Can add 2 numbers
# Can subtract 2 numbers
# Can multiply 2 numbers
# Can divide 2 numbers
# Taking it to the next level:
#
# Implement more complex operations, such as handling parentheses, exponentiation
# More advanced operations should continue to be broken into separate functions
#

from math_operations import *

# Main function to run the calculator
def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")
    print("6. Evaluate Expression")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice in ('1', '2', '3', '4', '5', '6'):
            if choice == '6':
                expression = input("Enter expression: ")
                print(f"Result: {evaluate_expression(expression)}")
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                elif choice == '5':
                    print(f"{num1} ^ {num2} = {exponentiate(num1, num2)}")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()