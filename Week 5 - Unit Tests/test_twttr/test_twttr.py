from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("ALLCAPS") == "LLCPS"
    assert shorten("w1th numb3rs") == "w1th nmb3rs"
    assert shorten("!punc.tuation?") == "!pnc.ttn?cd"