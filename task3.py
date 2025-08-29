"""
Write a function calculate_grade(score) that takes a student’s numeric score (an integer between 0 and 100) and returns their letter grade based on the following rules:
90–100 → A
80–89 → B
70–79 → C
60–69 → D
Below 60 → F
Make sure your function works for all boundary values (e.g., 60, 70, 80, 90, 100).

Expected output
print(calculate_grade(95))   # A
print(calculate_grade(88))   # B
print(calculate_grade(72))   # C
print(calculate_grade(65))   # D
print(calculate_grade(40))   # F
print(calculate_grade(100))  # A
print(calculate_grade(60))   # D
print(calculate_grade(70))   # C
print(calculate_grade(89))   # B
"""

def calculate_grade(score):
	if 90 <= score <= 100:
		return 'A'
	elif 80 <= score < 90:
		return 'B'
	elif 70 <= score < 80:
		return 'C'
	elif 60 <= score < 70:
		return 'D'
	elif 0 <= score < 60:
		return 'F'
	else:
		"Invalid Score"

