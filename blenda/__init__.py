# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
'Blenda for Python'
by Oskar Lundqvist /
Abrovinsch (c) 2018
"""

class Tokenizer:
    """Creates tokens from text"""
    def __init__(self, code):
        self.code = code

    def tokenize(self):
        return self.code.split(' ')
s
