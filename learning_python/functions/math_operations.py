

# ADDITION
def add(num1: float = 2, num2: float = 5) -> float:
    '''This function  **ADDS** numbers'''
    return num1 + num2


# SUBTRACTION
def subtract(num1: float = 2, num2: float = 5) -> float:
    '''This function  **SUBTRACTS** numbers'''
    return num1 - num2

# MULTIPLICATION
def multiply(num1: float = 2, num2: float = 5) -> float:
    '''This function  **MULTIPLIES** numbers'''
    return num1 / num2

# DIVISION
def divide(num1: float = 2, num2: float = 5) -> float:
    '''This function  **DIVIDES** numbers'''
    return num1 / num2

# EXPONENTIATION
def exponentiate(num1: float = 2, num2: float = 5) -> float:
    '''This function  **ELEVATES** numbers'''
    return num1 ** num2







# Function to handle parentheses (basic implementation)
def evaluate_expression(expression):
    try:
        return eval(expression)
    except Exception as e:
        return f"Error! {e}"