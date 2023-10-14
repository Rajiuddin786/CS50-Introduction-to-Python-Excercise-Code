from fuel import convert,gauge

def test_convert():
    assert convert("3/2")==(3, 2)
    assert convert("3/0")==(3,0)

def test_gauge():
    assert gauge(1,2)==50
    assert gauge(1,1)==100