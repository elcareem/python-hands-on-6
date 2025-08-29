"""
Task: School Attendance Tracker

Write a function check_attendance(students, present_list) that takes:
students: a list of all student names
present_list: a list of students who are present today
Return a dictionary with students as keys and "Present" or "Absent" as values

students = ["John", "Mary", "Peter", "Alice"]
present_list = ["John", "Alice"]
print(check_attendance(students, present_list))
Expected Output:

{'John': 'Present', 'Mary': 'Absent', 'Peter': 'Absent', 'Alice': 'Present'}

"""

students = ["John", "Mary", "Peter", "Alice"]
present_list = ["John", "Alice"]

def check_attendance(students, present_list):
	
	attendance = {}
	for student in students:
		if student in present_list:
			attendance.update({student: "Present"})
		elif student not in present_list:
	 		attendance.update({student: "Absent"})	

	return attendance

print(check_attendance(students, present_list))
