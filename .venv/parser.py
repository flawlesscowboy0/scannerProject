import json
from scanner import Scanner

class Token:
    def __init__(self, type, id, value):
        self.type = type
        self.id = id
        self.value = value

class Parser:
    def __init__(self, file_path):
        self.tokens = self.parse_tokens_from_file(file_path)

    def parse_tokens_from_file(self, file_path):
        tokens = []
        with open(file_path, 'r') as file:
            token_data = json.load(file)
            for data in token_data.values():
                token = Token(data['Type'], data['ID'], data['Value'])
                tokens.append(token)
        return tokens

    def print_token_hierarchy(self, token):
        hierarchy = ["Keywords", "Identifiers", "Operators", "Special Symbols", "String Literal", "Numeric Literal"]
        for level, token_type in enumerate(hierarchy):
            if token.type == token_type:
                print(f"Entering {' --> '.join(hierarchy[:level+1])}")
                if token.id == 503:
                    print(f"ID: {token.id}, Value: Newline Character")
                else:
                    print(f"ID: {token.id}, Value: {token.value}")
                print(f"Exiting {' --> '.join(reversed(hierarchy[:level+1]))}")
                break

    def print_tokens(self):
        for token in self.tokens:
            self.print_token_hierarchy(token)

if __name__ == "__main__":
    file_path = input("Enter a file path: ")
    scanner = Scanner(filepath=file_path)  # Invoke the scanner on the scl file.
    scanner.scan()
    parser = Parser("OutputTokens.json")  # We know the location of the file produced by the scanner.
    parser.print_tokens()