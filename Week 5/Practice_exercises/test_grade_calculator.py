import pytest
from grade_calculator import calculate_grade

def test_grade_a():
    assert calculate_grade(100) == 'A'
    assert calculate_grade(90) == 'A'
    assert calculate_grade(95) == 'A'

def test_grade_b():
    assert calculate_grade(89) == 'B'
    assert calculate_grade(80) == 'B'
    assert calculate_grade(85) == 'B'

def test_grade_c():
    assert calculate_grade(79) == 'C'
    assert calculate_grade(70) == 'C'
    assert calculate_grade(75) == 'C'

def test_grade_b():
    assert calculate_grade(69) == 'D'
    assert calculate_grade(60) == 'D'
    assert calculate_grade(65) == 'D'

def test_grade_f():
    assert calculate_grade(59) == 'F'
    assert calculate_grade(0) == 'F'
    assert calculate_grade(30) == 'F'

def test_inavlid_score_too_low():
    with pytest.raises(ValueError ,match='between 0 and 100'):
        calculate_grade(-1)

def test_inavlid_score_too_high():
    with pytest.raises(ValueError, match='between 0 and 100'):
        calculate_grade(101)



