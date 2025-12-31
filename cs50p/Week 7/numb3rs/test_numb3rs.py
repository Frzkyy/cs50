from numb3rs import validate


def test_valid_ip():
    assert validate("192.168.1.1") is True


def test_invalid_ip_out_of_range():
    assert validate("256.1.1.1") is False


def test_invalid_ip_structure():
    assert validate("192.168.1") is False


def test_invalid_ip_non_numeric():
    assert validate("a.b.c.d") is False

def test_invalid_later_octet():
    assert validate("1.256.1.1") is False
