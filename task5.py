"""
Employee Shift Manager
You are asked to build a small program to help manage employee work shifts in a company.  
Create a dictionary `shifts` where each key is an employee's name, and the value is a list of the days they are scheduled to work.  
     shifts = {
       "Alice": ["Monday", "Wednesday"],
       "Bob": ["Tuesday", "Thursday"],
       "Charlie": ["Monday", "Friday"]
   }


fucntion signature function add_shift(employee, day):
The  function should 
1. Checks if the employee exists in the dictionary.

 - If they exist, add the new day to their list (only if it’s not already there).

-  If they don’t exist, create a new key for them with the day inside a list.

-  Return the updated dictionary.


2. Write another function get_schedule(day) that:

Returns a list of employees working on that day.
"""


def add_shift(employee, day):
	shifts = {}

	days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
	if day in days:
		if employee in shifts:
			shifts[employee].append(day)
		else:
			shifts.update({employee: [day]})
	else:
		return "Day provided not valid"

	return shifts

