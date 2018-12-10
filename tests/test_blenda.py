import pytest
import blenda


# Test tokenizer
def test_tokenizer():
    x = blenda.Tokenizer(input('input code:'))
    tokens = x.tokenize()
    for t in tokens:
        print(t)

test_tokenizer()
