from plates import is_valid

def test_plates():
    assert is_valid("resj12")==True
    assert is_valid("asdfr12334")==False
    assert is_valid("Q123")==False
    assert is_valid("qw1er2")==False
    assert is_valid("QWE0")==False
    assert is_valid("9qwert")==False
    assert is_valid("qwe@34")==False