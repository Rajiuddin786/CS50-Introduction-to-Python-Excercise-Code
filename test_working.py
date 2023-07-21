import pytest
from working import convert

def test_convert():
    assert validate("9 AM to 10 PM") == "9:00 to 20:00"
    assert validate("12:00 AM to 12:00 PM") == "00:00 to 24:00

def test_value_error():
    with pytest.raise(ValueError):
        convert("9AM - 10PM")
