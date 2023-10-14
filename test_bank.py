import pytest
from bank import check

def test_check():
    assert check("Hello World")=="$0"
    assert check("Hi,Raj")=="$20"
    assert check("Raj is Good")=="$100"
    assert check("HI WORLD") == "$20"
    assert check("wassup world") == "$100"
    assert check("WASSUP WORLD") == "$10"