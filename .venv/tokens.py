# Tokens
tokenList = {
    "Keywords": {
        'import': 0,
        'implementations': 1,
        'function': 2,
        'main': 3,
        'return': 4,
        'type': 5,
        'integer': 6,
        'double': 7,
        'char': 8,
        'num': 9,
        'is': 10,
        'variables': 11,
        'define': 12,
        'of': 13,
        'begin': 14,
        'display': 15,
        'set': 16,
        'exit': 17,
        'endfun': 18,
        'symbol': 19,
        'end': 20,
        'input': 21,
        'structures': 22,
        'pointer': 23,
        'head': 24,
        'last': 25,
        'NULL': 26,
        'ChNode': 27,
        'using': 28,
        'reverse': 29,
        'while': 30,
        'endwhile': 31,
        'call': 32,
        'constants': 33,
        'float': 34,
        'array': 35,
        'for': 36,
        'to': 37,
        'do': 38,
        'endfor': 39,
        'string': 40,
        'specifications': 41,
        'struct': 42,
        'endstruct': 43,
        'definetype': 44,
        'declarations': 45,
        'parameters': 46,
        'void': 47,
        'destroy': 48
    },

    "Identifiers": {
        'x': 100,
        'r': 101,
        'area': 102,
        'cir': 103,
        'pchar': 104,
        'j': 105,
        'N': 106,
        'sum': 107,
        'ave': 108,
        'svalue': 109,
        'num': 110,
        'basic': 111,
        'lib': 112,
        'linked': 113,
        'Datablock': 114,
        'stname': 115,
        'age': 116,
        'jobcode': 117,
        'DataT': 118,
        'make': 119,
        'dblock': 120,
        'nname': 121,
        'nage': 122,
        'njobcode': 123,
        'data': 124,
        'stdio': 125
    },

    "Operators": {
        '+': 300,
        '-': 301,
        '*': 302,
        '/': 303,
        '^': 304,
        '>': 305,
        '<': 306,
        '"': 407,
        '=': 408,
        'add': 409,
        ':': 410
    },

    "Special Symbols": {
        '.': 500,
        ',': 501,
        'PI': 502,
        'M_PI': 503,
        '[N]': 504,
        '\n': 505,
        '\t': 506,
        'scl': 507,
        '_': 508,
        '[': 509,
        ']': 510
    }
}


class Token:
    def __init__(self, type, id, value):
        self.type = type
        self.id = id
        self.value = value

    def getData(self):
        return [self.type, self.id, self.value]
