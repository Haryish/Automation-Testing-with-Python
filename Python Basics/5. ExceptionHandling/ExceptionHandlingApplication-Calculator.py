class FormulaError(Exception):
    """Custom exception for formula errors"""
    pass


def parse_input(user_input):
    """Parse user input into two numbers and an operator"""
    input_list = user_input.split()
    if len(input_list) != 3:
        raise FormulaError('Input does not consist of three elements. Suggested to provide spaces between inputs')
    n1, op, n2 = input_list
    try:
        n1, n2 = float(n1), float(n2)
    except ValueError:
        raise FormulaError('The first and third input value must be numbers')
    return n1, op, n2


def calculate(n1, op, n2):
    """Perform the calculation based on the operator"""
    try:
        match op:
            case '+':
                return n1 + n2
            case '-':
                return n1 - n2
            case '*':
                return n1 * n2
            case '/':
                if n2 == 0:
                    raise ZeroDivisionError('Cannot divide by zero')
                return n1 / n2
            case _:
                # Handles any operator that isn't recognized
                raise FormulaError(f'Operator "{op}" is not valid')
    except ZeroDivisionError as e:
        # Catch zero division error and display appropriate message
        print(e)
        return None
    except FormulaError as e:
        # Handle invalid operator error and display message
        print(e)
        return None


while True:
    user_input = input('>>> ')
    if user_input == 'quit':
        print("Exiting the program.")
        break
    try:
        n1, op, n2 = parse_input(user_input)  # Parse the input and validate
        result = calculate(n1, op, n2)  # Perform the calculation
        if result is not None:
            print(result)  # Only print the result if it is valid
    except FormulaError as e:
        print(f"Error: {e}")
