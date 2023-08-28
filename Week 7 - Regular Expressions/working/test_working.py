from working import convert
import pytest


def test_format():
    with pytest.raises(ValueError):
        convert("6 AM - 5 PM")

def test_values():
    with pytest.raises(ValueError):
        convert("13 AM to 17 PM")
        convert("5:69 AM to 6:80 PM")


def test_output():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:00 PM to 6:00 AM") == "22:00 to 06:00"