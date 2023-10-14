from bank import check

def test_check():
    assert check("Hello")=="$100"
    assert check("Hi")=="$20"
    assert check("Raj")=="$0"
    assert check("HI WORLD") == "$20"
    assert check("wassup world") == "$100"
    assert check("WASSUP WORLD") == "$10"