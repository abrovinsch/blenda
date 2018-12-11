import pytest
import blenda


# Test tokenizer
def test_tokenizer(code):
    tokenizer = blenda.Tokenizer(code)
    tokens = tokenizer.tokenize()
    for t in tokens:
        print(t)

    parser = blenda.Parser(tokens)
    for n in parser.parse():
        print(n)

#test_tokenizer()

f = blenda.load_blenda_file("tests/testcode.blenda")
test_tokenizer(f)
