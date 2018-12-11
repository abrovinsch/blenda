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
    print("Loaded %s" % path)
    return file.read()

class Token:
    """Represents a single token"""
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'TOKEN(type: %s, value: %s)' % (self.type, self.value)

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
        'comma':r',',
        'newline':r'\\n',
        'identifier':r'\b\w+\b',
        'string':r'"[^"]+"'
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
                if type == 'string':
                    val = val[1:-1]
                return Token(type, val)

        raise RuntimeError('Couldnt match token on "%s"' % self.code)

    def tokenize(self):
        while self.code != '':
            self.code = self.code.strip()
            t = self.tokenize_one_token()
            self.tokens.append(t)
        return self.tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.nodes = []

    def consume(self, expected_type):
        token = self.tokens.pop(0)
        if token.type == expected_type:
            return token
        else:
            raise RuntimeError('Expected token of type %s, got %s with value "%s"' % (expected_type, token.type, token.value))

    def peek(self, expected_type, offset=0):
        return self.tokens[offset].type == expected_type

    def parse_talker(self):
        name = self.consume('identifier').value
        words = []
        children = []

        self.consume('obracket')
        while not self.peek('cbracket'):
            if self.peek('string'):
                words.extend(self.parse_string_list())
            elif self.peek('identifier'):
                x = self.parse_talker()
                children.append(x)

        self.consume('cbracket')
        return Talker(name, words, children)

    def parse_string_list(self):
        strings = []
        if self.peek('string'):
            strings.append(self.consume('string').value)
            while self.peek('string'):
                strings.append(self.consume('string').value)
        return strings

    def parse(self):
        while len(self.tokens):
            self.nodes.append(self.parse_talker())

        return self.nodes

class Talker:
    def __init__(self, name, words, children=[]):
        self.name = name
        self.words = words
        self.children = children

    def __str__(self):
        children_text = []
        for c in self.children:
            children_text.append(str(c))
        return 'TALKER(name="%s" words=%s children=%s)' % (self.name, self.words, children_text)
