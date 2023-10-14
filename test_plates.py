from plates import is_valid

def test_plates():
    assert is_valid("resj12")==True
    assert is_valid("asdfr12334")==False