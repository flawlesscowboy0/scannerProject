"""
Logical Steps:

    1. Read entire file into string.
    2. Split string into tokens along the following lines:
        a. All words with letters only.
        b. All words with numbers only.
        c. All punctuation/operators (,.!@#$%^&*()+=-_[]{}/?'";:<>) either in singleton form or repeated.
        d. Special characters which are unprintable such as \n and \t.
    3. Tokens will be stored in a list, which is then iterated over as list items are compared against a dictionary.
    4. Successful (or not) comparison against the dictionary entries produces the full form of the token for inclusion
       in the JSON file which is produced.
"""

import sys
import json
import re
from tokens import *
from pathlib import Path

# Experimental command line argument acceptance.
sysArgv = sys.argv
if len(sysArgv) > 1:
    # Accepts command line arguments of the form - py ./scanner.py ./file_to_be_scanned
    text = Path(sysArgv[1]).read_text()  # Reads entire file into text object from command line.
else:
    path = input("Enter path of file you wish to scan: ")
    text = Path(path).read_text()  # Reads entire file into text object from user prompt.
# This regex captures all tokens properly, no longer any issues with whitespace.
wordList = re.findall(r'"[^"]*"|[a-zA-Z_]+|\d+\.\d+|\t|\n|[/*,=]+|[:.]+|[\[\]<>+\-$%&()]+', text)

"""Prototyping the logic to parse the list.

commentBlock updates only on hitting block comment notation. If true, no tokens should be scanned."""
commentBlock = False
inlineComment = False
stringLiteral = False
masterTokenList = []
for word in wordList:
    if word == "/*" or word == "description":
        commentBlock = True
    elif word == "*/":
        commentBlock = False
        continue
    elif word == "//":
        inlineComment = True
    elif word == "\n":
        inlineComment = False
    elif word.startswith('"'):
        stringLiteral = True

    # Begin comparison logic.
    if not commentBlock and not inlineComment:
        # Logic to compare list elements against token dictionary should go here.
        if stringLiteral:
            strippedWord = word.strip('"')
            newToken = Token('String Literal', 2222, strippedWord)
            stringLiteral = False
        elif re.match(r"^[0-9]+(\.[0-9]+)?$", word):
            newToken = Token('Numeric Literal', 1111, word)
        elif word in tokenList["Keywords"]:
            newToken = Token('Keywords', tokenList["Keywords"][word], word)
        elif word in tokenList["Identifiers"]:
            newToken = Token('Identifiers', tokenList["Identifiers"][word], word)
        elif word in tokenList["Operators"]:
            newToken = Token('Operators', tokenList["Operators"][word], word)
        elif word in tokenList["Special Symbols"]:
            newToken = Token('Special Symbols', tokenList["Special Symbols"][word], word)
        elif word in tokenList["EOS"]:
            newToken = Token('End of Statement', tokenList["EOS"][word], 'EOS')
        else:
            newToken = Token('Unknown Token', 7777, word)

        print("New Token Created: ", newToken.getData())  # Print that token was made to console, along with data.
        masterTokenList.append(newToken)  # Add token to master list.
    # Example File has a new token made here, "End of Statement" but we capture \n so not sure if necessary.


# Create JSON file
# Helper method to convert list to dictionary.
def create_dictionary(a):
    dictObj = iter(a)
    return dict(zip(dictObj, dictObj))
    # Zip takes the iterable objects out of the passed in list in pairs, creating a new dictionary object out of them.


# Condensed this all into one section.
json_output = open("OutputTokens.json", "w")  # Open file for writing.
masterDictionary = {}  # Create empty dictionary.
counter = 0
for Token in masterTokenList:
    tokenID = "Token " + counter.__str__()  # Generate token ID using counter.
    masterDictionary.update({tokenID: {}})  # Add Token sub-dictionary to the master dictionary.
    tokenData = Token.getData()
    dataList = ['Type', tokenData[0], 'ID', tokenData[1], 'Value', tokenData[2]]
    tokenDataDictionary = create_dictionary(dataList)  # Create the sub-dictionary.
    masterDictionary[tokenID].update(tokenDataDictionary)  # Insert sub-dictionary to the correct Token location.
    counter += 1

json_data = json.dumps(masterDictionary, indent=4)
json_output.write(json_data)  # Create data object and write to file.
