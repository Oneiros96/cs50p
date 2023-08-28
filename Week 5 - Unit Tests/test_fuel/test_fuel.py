from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("4/4") == 100
    assert convert("3/6") == 50
    with pytest.raises(ValueError):
        convert("cat/cat")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"