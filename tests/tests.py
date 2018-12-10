import pytest
import blenda

# Test tokenizer
x = blenda.Tokenizer('abc de')
print(', '.join(x.tokenize()))
