'''
Calculate letter grade from numeric score 

A: 90-100
B: 80-89
C: 70-79
D: 60-69
E: 0-59
'''

def calculate_grade(score):

    if score < 0 or score > 100:
        raise ValueError('Score must be between 0 and 100')

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else: 
        return 'F'
    
    