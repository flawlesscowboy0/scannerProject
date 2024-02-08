"""
Logical Steps:

    1. Read entire file into string.
    2. Split string into words (tokens) and prepare for processing. NOTE: Need to determine fate/handling of special
    characters like \n amd \t.
    3. Once list of words is prepared, compare against token dictionary and update attributes (identifier, keyword, etc)
    NOTE: Probably useful to simply convert string objects in list to list objects in list (which themselves hold
    strings) for easy handling of attributes.
    4. Once all tokens are properly tagged, produce JSON file from list.
    5. Ensure all output is correctly displayed and JSON file is produced correctly.

    Reading the entire file into a list allows us to iterate over the list and easily handle comments both at the end of
    a line and as a block. (See prototype logic below for an idea of how block comments can be handled via this method.
    For end of line comments the implementation will be to check for \n after them which would imply the end of the
    comment.)

    Currently, need to implement a dictionary or devise a regex capable of parsing for the types of characters we are
    interested in parsing. Need to implement comparison against dictionary.
"""

import json
import pprint
import re

from pathlib import Path

path = input("Enter path of file you wish to scan: ")
text = Path(path).read_text()  # Reads entire file into text object.
wordList = re.split(r"([A-Za-z]+|[0-9]+|\t+|\n+|[/*,=]+|[\":.]+|[+\-$%&()])",
                    text)  # This regex captures all tokens properly.
"""
Unfortunately, the regex above captures tokens *too* well, and we end up with a variety of weird whitespace in the list.
The lines below simply remove the remaining empty strings so that pprint will not display them and they will not be
errantly entered into the JSON or as an "unknown" token.

Considered solutions:

''.join().split() - This can remove errant leftover whitespace, but you also lose \n and \t.
Could look into filter(), list comprehension, or lambda.

The iterating whitespace eater below is as elegant as it gets for now.
"""
count = ""
while len(count) < 32:  # Arbitrary length, could be easily adjusted to capture even more whitespace.
    while count in wordList:
        wordList.remove(count)
    count += " "  # Append one more space to each iteration of the loop.
pprint.pprint(wordList)  # This will pretty print the list. If split along whitespace, \n and \t will be shown.

"""Prototyping the logic to parse the list.

commentBlock updates only on hitting block comment notation. If true, no tokens should be scanned."""
from tokens import *

commentBlock = False
inlineComment = False
masterTokenList = []
for word in wordList:
    if word == "/*":
        commentBlock = True
    elif word == "*/":
        commentBlock = False
        continue
    elif word == "//":
        inlineComment = True
    elif word == "\n":
        inlineComment = False

    # Begin comparison logic.
    if not commentBlock and not inlineComment:
        # Logic to compare list elements against token dictionary should go here.
        if word in tokenList["Keywords"]:
            newToken = Token('Keywords', tokenList["Keywords"][word], word)
        elif word in tokenList["Identifiers"]:
            newToken = Token('Identifiers', tokenList["Identifiers"][word], word)
        elif word in tokenList["Operators"]:
            newToken = Token('Operators', tokenList["Operators"][word], word)
        elif word in tokenList["Special Symbols"]:
            newToken = Token('Special Symbols', tokenList["Special Symbols"][word], word)
        elif word.isdigit():
            newToken = Token('Numbers', 1111, word)
        else:
            newToken = Token('Unknown Token', 7777, word)

        print("New Token Created: ", newToken.getData())  # Print that token was made to console, along with data.
        masterTokenList.append(newToken)  # Add token to master list.
    # Example File has a new token made here, "End of Statement" but we capture \n so not sure if necessary.

# Create JSON file

json_output = open("OutputTokens.json", "w")  # Open file for writing.
masterDictionary = {}  # Create empty dictionary.
counter = 0
for Token in masterTokenList:
    tokenID = "Token " + counter.__str__()  # Generate token ID using counter.
    masterDictionary.update({tokenID: {}})
    counter += 1


# Helper method to convert list to dictionary.
def create_dictionary(a):
    dictObj = iter(a)
    return dict(zip(dictObj, dictObj))
    # Zip takes the iterable objects out of the passed in list in pairs, creating a new dictionary object out of them.


counter = 0  # Reset the clock
for Token in masterTokenList:
    tokenData = Token.getData()
    dataList = ['Type', tokenData[0], 'ID', tokenData[1], 'Value', tokenData[2]]
    tokenDataDictionary = create_dictionary(dataList)

    tokenID = "Token " + counter.__str__()  # Make ID same as before.
    masterDictionary[tokenID].update(tokenDataDictionary)
    counter += 1

json_data = json.dumps(masterDictionary, indent=4)
json_output.write(json_data)  # Create data object and write to file.
