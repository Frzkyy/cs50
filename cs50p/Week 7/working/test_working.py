import pytest
from working import convert


def test_simple_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_with_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_evening_to_morning():
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"

def test_evening_to_morning_with_minutes():
    assert convert("8:00 PM to 8:00 AM") == "20:00 to 08:00"

def test_noon_and_midnight():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_noon_and_midnight_with_minutes():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_minutes_not_off_by_five():
    assert convert("10:01 AM to 11:59 AM") == "10:01 to 11:59"

def test_missing_to():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")

def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")

def test_missing_space():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("09 AM to 5:001 PM")

def test_24_hour_time_not_allowed():
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")

def test_wrong_separator():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_single_digit_minutes():
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")
