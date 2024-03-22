# Tokens
tokenList = {
    "Keywords": {
        'imports': 0,
        'implementations': 1,
        'function': 2,
        'main': 3,
        'return': 4,
        'type': 5,
        'integer': 6,
        'is': 7,
        'variables': 8,
        'define': 9,
        'of': 10,
        'double': 11,
        'begin': 12,
        'display': 13,
        'set': 14,
        'exit': 15,
        'endfun': 16
    },

    "Identifiers": {
        'x': 100
    },

    "Operators": {
        '=': 300
    },

    "Special Symbols": {
        ',': 500
    },

    "EOS": {
        '\n' : 1000
    }
}


class Token:
    def __init__(self, type, id, value):
        self.type = type
        self.id = id
        self.value = value

    def getData(self):
        return [self.type, self.id, self.value]
