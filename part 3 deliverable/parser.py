import json
from scanner import Scanner

# Define constants
HIERARCHY = ["Keywords", "Identifiers", "Operators", "Special Symbols/String Literal/Numeric Literal"]
OUTPUT_TOKENS_FILE = "OutputTokens.json"

class Token:
    """Class to represent tokens."""
    def __init__(self, type, id, value):
        self.type = type
        self.id = id
        self.value = value

class Parser:
    """Class to parse tokens from a JSON file."""
    def __init__(self, file_path=None):
        if file_path:
            self.file_path = file_path
            self.invoke_from_another_class()
        else:
            self.file_path = OUTPUT_TOKENS_FILE
            self.tokens = self.parse_tokens_from_file(self.file_path)

    def invoke_from_another_class(self):
        """Invoked when called from another class."""
        scanner = Scanner(filepath=self.file_path)
        print("\n\nParser Output Begins:\n\n")
        self.file_path = OUTPUT_TOKENS_FILE
        self.tokens = self.parse_tokens_from_file(self.file_path)
        self.print_tokens()
        print("\n\nInterpreter Output Begins:\n\n")

    def parse_tokens_from_file(self, file_path):
        """Parse tokens from the given JSON file."""
        try:
            with open(file_path, 'r') as file:
                token_data = json.load(file)
                tokens = [Token(data['Type'], data['ID'], data['Value']) for data in token_data.values()]
        except FileNotFoundError:
            print("File not found.")
            tokens = []
        except json.JSONDecodeError:
            print("Error decoding JSON.")
            tokens = []
        return tokens

    def print_token_hierarchy(self, token):
        """Print the hierarchy and details of a token."""
        for level, token_types in enumerate(HIERARCHY):
            if token.type in token_types.split("/"):
                break

        if "/" in HIERARCHY[level]:
            combined_levels = HIERARCHY[level].split("/")
            combined_level_index = combined_levels.index(token.type)
            enter_tags = " --> ".join(HIERARCHY[:level] + [combined_levels[combined_level_index]])
            exit_tags = " --> ".join(reversed(HIERARCHY[:level] + [combined_levels[combined_level_index]]))
        else:
            enter_tags = " --> ".join(HIERARCHY[:level + 1])
            exit_tags = " --> ".join(reversed(HIERARCHY[:level + 1]))

        print(f"Entering {enter_tags}")
        if token.id == 503:
            print(f"ID: {token.id}, Value: Newline Character")
        else:
            print(f"ID: {token.id}, Value: {token.value}")
        print(f"Exiting {exit_tags}")

    def print_tokens(self):
        """Print the hierarchy and details of all tokens."""
        for token in self.tokens:
            self.print_token_hierarchy(token)

if __name__ == "__main__":
    file_path = input("Enter a file path: (Do not use quotation marks) ")
    parser = Parser(file_path)
    parser.print_tokens()
