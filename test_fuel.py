from fuel import convert,gauge

def test_convert():
    assert convert("3/2")==(3, 2)