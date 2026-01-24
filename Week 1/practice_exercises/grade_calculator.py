"""
Exercise 2: Grade Calculator
Challenge:
Build a program that calculates a student's final grade based on multiple test scores.
Requirements:

Ask the user for their name
Get 5 test scores (0-100)
Store the scores in a list
Calculate the average
Use if statements to assign a letter grade:

A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: Below 60


Display the student's name, all scores, average, and letter grade

Hints:

Use a list to store scores
Use sum(list) and len(list) to calculate average
Use if/elif/else for letter grades

Sample Output:
Student Name: John Smith
Test Scores: [85, 92, 78, 88, 95]
Average: 87.6
Letter Grade: B
"""

# define variables for user input
student_name = input("Enter the student's name: ")
test_scores = []

# get 5 test scores from the user
for  score in range(1,6):
    score= float(input(f"Enter score {score} :"))
    test_scores.append(score)
                 
# calculate student's average score
average_score = sum(test_scores) / len(test_scores)

# Determine letter grade based on average score

if 90 <= average_score <= 100:
    letter_grade = "A"
elif 80 <= average_score < 90:
    letter_grade = "B"
elif 70 <= average_score < 80:
    letter_grade = "C"
elif 60 <= average_score < 70:
    letter_grade = "D"
else:
    letter_grade = "F"


# Display student details
print("\n\nStudent Name:", student_name)
print("Test Scores:", test_scores)
print("Average:", average_score)
print("Letter Grade:", letter_grade)                                                     




