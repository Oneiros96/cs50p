import pytest
from jar import Jar

def test_init():
    with pytest.raises(ValueError):
        Jar(0)
        Jar(-1)
        Jar("12")
    assert Jar(10).capacity == 10
    assert Jar(42).capacity == 42
    assert Jar().size == 0

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.deposit(100)

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(1)
    assert jar.size == 9
    jar.withdraw(2)
    assert jar.size == 7
    with pytest.raises(ValueError):
        jar.withdraw(100)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"



