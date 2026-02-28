import pytest
from temp_converter import celsius_to_fahrenheit

def test_freeze_point():
    assert celsius_to_fahrenheit(0) == 32

def test_boiling_point():
    assert celsius_to_fahrenheit(100) == 212

def test_negative_celsius():
    assert celsius_to_fahrenheit(-40)

def test_room_temperature():
    assert celsius_to_fahrenheit(20) == 68