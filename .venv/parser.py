import json

class Token:
    def __init__(self, type, id, value):
        self.type = type
        self.id = id
        self.value = value

# Parse the JSON file containing token data
def parse_tokens_from_file(file_path):
    tokens = []

    with open(file_path, 'r') as file:
        token_data = json.load(file)
        
        for key, data in token_data.items():
            type = data['Type']
            id = data['ID']
            value = data['Value']

            token = Token(type, id, value)
            tokens.append(token)

    return tokens

# Example usage
file_path = input("Enter a file path")  # Update with the path to your output file
tokens = parse_tokens_from_file(file_path)

# Print the parsed tokens
for token in tokens:
    if (token.type == "Keywords"):
        print("Entering <Keywords>")
        print(f"ID: {token.id}, Value: {token.value}")
        print("Exiting <Keywords>")
        continue
    elif (token.type == "Identifiers"):
        print("Entering <Keywords>")
        print("Entering <Identifiers>")
        print(f"ID: {token.id}, Value: {token.value}")
        print("Exiting <Identifiers>")
        print("Exiting <Keywords>")
        continue
    elif (token.type == "Operators"):
        print("Entering <Keywords>")
        print("Entering <Identifiers>")
        print("Entering <Operators>")
        print(f"ID: {token.id}, Value: {token.value}")
        print("Exiting <Operators>")
        print("Exiting <Identifiers>")
        print("Exiting <Keywords>")
        continue
    elif (token.type == "Special Symbols"):
        print("Entering <Keywords>")
        print("Entering <Identifiers>")
        print("Entering <Operators>")
        print("Entering <Special Symbols>")
        print(f"ID: {token.id}, Value: {token.value}")
        print("Exiting <Special Symbols>")
        print("Exiting <Operators>")
        print("Exiting <Identifiers>")
        print("Exiting <Keywords>")
        continue
    elif (token.type == "String Literal"):
        print("Entering <Keywords>")
        print("Entering <Identifiers>")
        print("Entering <Operators>")
        print("Entering <String Literal>")
        print(f"ID: {token.id}, Value: {token.value}")
        print("Exiting <String Literal>")
        print("Exiting <Operators>")
        print("Exiting <Identifiers>")
        print("Exiting <Keywords>")
        continue
    elif (token.type == "Numeric Literal"):
        print("Entering <Keywords>")
        print("Entering <Identifiers>")
        print("Entering <Operators>")
        print("Entering <Numeric Literal>")
        print(f"ID: {token.id}, Value: {token.value}")
        print("Exiting <Numeric Literal>")
        print("Exiting <Operators>")
        print("Exiting <Identifiers>")
        print("Exiting <Keywords>")
        continue