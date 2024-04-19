import sys
import json
import re
from tokens import *
from pathlib import Path

class Scanner:
    def __init__(self, filepath=None):
        self.text = self._read_file(filepath) if filepath else self._read_from_input()
        self.word_list = self._tokenize()
        self.scan()

    def _read_file(self, filepath):
        return Path(filepath).read_text()

    def _read_from_input(self):
        path = input("Enter path of file you wish to scan: ")
        return Path(path).read_text()

    def _tokenize(self):
        return re.findall(r'"[^"]*"|[a-zA-Z_]+|\d+\.\d+|\t|\n|[/*,=]+|[:.]+|[\[\]<>+\-$%&()]+', self.text)

    def _create_dictionary(self, a):
        dict_obj = iter(a)
        return dict(zip(dict_obj, dict_obj))

    def scan(self):
        comment_block = False
        inline_comment = False
        string_literal = False
        master_token_list = []

        for word in self.word_list:
            if word == "/*" or word == "description":
                comment_block = True
            elif word == "*/":
                comment_block = False
                continue
            elif word == "//":
                inline_comment = True
            elif word == "\n":
                inline_comment = False
            elif word.startswith('"'):
                string_literal = True

            if not comment_block and not inline_comment:
                if string_literal:
                    stripped_word = word.strip('"')
                    new_token = Token('String Literal', 2222, stripped_word)
                    string_literal = False
                elif re.match(r"^[0-9]+(\.[0-9]+)?$", word):
                    new_token = Token('Numeric Literal', 1111, word)
                elif word in tokenList["Keywords"]:
                    new_token = Token('Keywords', tokenList["Keywords"][word], word)
                elif word in tokenList["Identifiers"]:
                    new_token = Token('Identifiers', tokenList["Identifiers"][word], word)
                elif word in tokenList["Operators"]:
                    new_token = Token('Operators', tokenList["Operators"][word], word)
                elif word in tokenList["Special Symbols"]:
                    new_token = Token('Special Symbols', tokenList["Special Symbols"][word], word)
                elif word in tokenList["EOS"]:
                    new_token = Token('End of Statement', tokenList["EOS"][word], 'EOS')
                else:
                    new_token = Token('Unknown Token', 7777, word)

                print("New Token Created: ", new_token.getData())
                master_token_list.append(new_token)

        master_dictionary = {}
        counter = 0
        for token in master_token_list:
            token_id = "Token " + str(counter)
            master_dictionary[token_id] = {}
            token_data = token.getData()
            data_list = ['Type', token_data[0], 'ID', token_data[1], 'Value', token_data[2]]
            token_data_dictionary = self._create_dictionary(data_list)
            master_dictionary[token_id].update(token_data_dictionary)
            counter += 1

        json_data = json.dumps(master_dictionary, indent=4)
        with open("OutputTokens.json", "w") as json_output:
            json_output.write(json_data)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        scanner = Scanner(filepath=sys.argv[1])  # Instantiate Scanner with filepath argument
    else:
        scanner = Scanner()
    scanner.scan()
