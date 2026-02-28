import pytest
from password_validator import is_valid_password

def test_password_valid():
    assert is_valid_password('Password1') is True

def test_password_too_short():
    assert is_valid_password('Pass1') is False

def test_password_no_uppercase():
    assert is_valid_password('password1') is False

def test_password_no_lowercase():
    assert is_valid_password('PASSWORD1') is False

def test_password_no_digit():
    assert is_valid_password('Password') is False

def test_all_requirements_met():
    assert is_valid_password('SECUREpass123') is True
