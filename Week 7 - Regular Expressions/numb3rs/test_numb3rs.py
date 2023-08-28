from numb3rs import validate

def test_false_inputs():
    assert validate("cat") == False
    assert validate("1.2.3") == False
    assert validate("cat.dog") == False
    assert validate("256.1.1.1") == False
    assert validate("1.300.1.1") == False

def test_true_inputs():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("123.45.67.89") == True
    assert validate("3.81.245.248") == True