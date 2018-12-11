# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
'Blenda for Python'
by Oskar Lundqvist /
Abrovinsch (c) 2018
"""

import re
import codecs

def load_blenda_file(path):
    file = open(path)
    return file.read()

class Token:
    """Represents a single token"""
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'TOKEN[ type: %s, value: %s]' % (self.type, self.value)

class Tokenizer:
    """Creates tokens from text"""
    TOKEN_TYPES = {
        'oparen':r'\(',
        'cparen':r'\)',
        'obracket':r'\{',
        'cbracket':r'\}',
        'osqbracket':r'\[',
        'csqbracket':r'\]',
        'lessthan':r'\<',
        'greaterthan':r'\>',
        'semicolon':r';',
        'at':r'@',
        'dot':r'\.',
        'newline':r'\\n',
        'identifier':r'\b\w+\b',
        'string':r'\"(.*)\"'
    }

    def __init__(self, code):
        self.code = code
        self.tokens = []

    def tokenize_one_token(self):
        for type, regex in self.TOKEN_TYPES.items():
            r = r'{0}({1})'.format('^',regex)
            re.compile(r, re.U)
            z = re.match(r, self.code)

            if(z):
                val = z.groups()[0]
                self.code = self.code[len(val):]
                return Token(type, val)

        raise RuntimeError('Couldnt match token on "%s"' % self.code)

    def tokenize(self):
        while self.code != '':
            self.code = self.code.strip()
            self.tokens.append(self.tokenize_one_token())
        return self.tokens
