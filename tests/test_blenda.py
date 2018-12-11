import pytest
import blenda


# Test tokenizer
def test_tokenizer(code):
    x = blenda.Tokenizer(code)
    tokens = x.tokenize()
    for t in tokens:
        print(t)

#test_tokenizer()

f = blenda.load_blenda_file("tests/testcode.blenda")
test_tokenizer(f)
