import math

# Symbol table to store variables
symbol_table = {}

# Constants
symbol_table["PI"] = math.pi
symbol_table["M_PI"] = math.pi

# Function to handle input statement
def handle_input(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return handle_input(prompt)

# Function to handle display statement
def handle_display(message, value):
    print(message, value)

# Function to execute SCL statements
def execute_statement(statement):
    if statement[0] == "input":
        variable_name = statement[1]
        prompt = statement[2]
        value = handle_input(prompt)
        symbol_table[variable_name] = value
    elif statement[0] == "display":
        message = statement[1]
        if statement[2] in symbol_table:
            value = symbol_table[statement[2]]
        else:
            value = float(statement[2]) if statement[2].replace(".", "", 1).isdigit() else statement[2]
        handle_display(message, value)

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
        if statement[0] == "input" or statement[0] == "display":
            execute_statement(statement)
        elif statement[0] == "set":
            variable_name = statement[1]
            expression = statement[2]
            value = evaluate_expression(expression)
            symbol_table[variable_name] = value
        else:
            raise ValueError("Invalid statement: {}".format(statement))

# Example SCL code
scl_code = [
    ["input", "r", "Enter value of radius: "],
    ["display", "Value of radius:", "r"],
    ["set", "area", ["multiply", ["variable", "PI"], ["power", ["variable", "r"], ["number", "2"]]]],
    ["set", "cir", ["multiply", ["number", "2.0"], ["multiply", ["variable", "PI"], ["variable", "r"]]]],
    ["display", "Value of area:", "area"],
    ["display", "Value of circumference:", "cir"]
]

# Execute the SCL code
execute_scl(scl_code)
