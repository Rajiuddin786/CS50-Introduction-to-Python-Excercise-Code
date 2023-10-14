from bank import check

def test_check():
    assert(check("Hello"))==-1
    assert(check("Hi"))==0
    assert(check("Raj"))==1