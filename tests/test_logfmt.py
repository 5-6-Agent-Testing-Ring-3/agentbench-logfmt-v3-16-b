from logfmt import decode, encode

def test_roundtrip():
    d = {"level": "info", "msg": "hello world", "n": "3"}
    assert decode(encode(d)) == d

def test_quoted_value():
    assert decode('msg="a b"') == {"msg": "a b"}
