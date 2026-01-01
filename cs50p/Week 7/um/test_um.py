import pytest
from um import count

def test_single_um():
    assert count("um") == 1

def test_multiple_um():
    assert count("um um um") == 3

def test_mixed_case_um():
    assert count("Um uM UM") == 3

def test_um_not_in_word():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrella") == 0

def test_um_in_sentence():
    assert count("hello, um, world") == 1
    assert count("um? yes, um!") == 2

def test_um_with_punctuation():
    assert count("um, um.") == 2
    assert count("um! um?") == 2

def test_um_without_spaces():
    assert count("um,um") == 2
    assert count("um.um") == 2

def test_empty_string():
    assert count("") == 0

def test_no_um():
    assert count("hello world") == 0
