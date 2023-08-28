from plates import is_valid

def test_len():
    #lenght
    assert is_valid("t") == False
    assert is_valid("toloong") == False

    # dont starts with 2 letters
    assert is_valid("23") == False
    assert is_valid("!?") == False
    assert is_valid("  test") == False

    # numbers at the end not starting with 0
    assert is_valid("te0123") == False
    assert is_valid("te123s") == False
    
    # all num values
    assert is_valid("te 123") == False
    assert is_valid("te!?50") == False

    assert is_valid("te1234") == True


