from um import count

def test_1():
    assert count("um") == 1
def test_2():
    assert count("yummy") == 0
def test_3():
    assert count("Hello um, um...i um? Um!") == 4
