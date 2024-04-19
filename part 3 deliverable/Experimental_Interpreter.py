import math

# Symbol table to store variables
symbol_table = {}

# Constants
symbol_table["PI"] = math.pi
symbol_table["M_PI"] = math.pi

# Function to handle display statement
def handle_display(*args):
    print(*args)

# Function to execute SCL statements
def execute_statement(statement):
    if statement[0] == "display":
        message = statement[1]
        args = [symbol_table[arg] if arg in symbol_table else arg for arg in statement[2:]]
        handle_display(message, *args)
    elif statement[0] == "set":
        variable_name = statement[1]
        expression = statement[2]
        value = evaluate_expression(expression)
        symbol_table[variable_name] = value
    else:
        raise ValueError("Invalid statement: {}".format(statement))

# Function to evaluate expressions
def evaluate_expression(expression):
    if expression[0] == "add":
        return evaluate_expression(expression[1]) + evaluate_expression(expression[2])
    elif expression[0] == "subtract":
        return evaluate_expression(expression[1]) - evaluate_expression(expression[2])
    elif expression[0] == "multiply":
        return evaluate_expression(expression[1]) * evaluate_expression(expression[2])
    elif expression[0] == "divide":
        return evaluate_expression(expression[1]) / evaluate_expression(expression[2])
    elif expression[0] == "power":
        return evaluate_expression(expression[1]) ** evaluate_expression(expression[2])
    elif expression[0] == "number":
        return float(expression[1])
    elif expression[0] == "variable":
        if expression[1] in symbol_table:
            return symbol_table[expression[1]]
        else:
            raise ValueError("Undefined variable: {}".format(expression[1]))

# Function to execute SCL code
def execute_scl(code):
    for statement in code:
        execute_statement(statement)

# Example SCL code
scl_code = [
    ["display", "Welcome to the world of SCL"],
    ["set", "x", ["number", "45.95"]],
    ["display", "Value of x:", "x"]
]

# Execute the SCL code
execute_scl(scl_code)
