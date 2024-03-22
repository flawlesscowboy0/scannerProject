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
    print(f"Type: {token.type}, ID: {token.id}, Value: {token.value}")