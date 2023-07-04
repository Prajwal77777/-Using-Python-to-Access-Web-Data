from twttr import shorten


def test_shortens():
    assert shorten("") == ""
    assert shorten("hello") == "hll"
    assert shorten("aeiou") == ""
    assert shorten("hello world1") == "hll wrld1"
