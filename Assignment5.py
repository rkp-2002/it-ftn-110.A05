# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <K,Pelayo>,<11/10/23>, <continuing script>
# ------------------------------------------------------------------------------------------ #
import json
file=None
# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str ="Enrollments.json"
 # Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
#row of student data
student_row1: dict[str,str] = {f"Firstname":student_first_name, "Lastname" :student_last_name, "course" :course_name}
student_row2: dict[str,str] = {f"Firstname":student_first_name, "Lastname" :student_last_name, "course" :course_name}
students: list[dict[str,str]] = [student_row1,student_row2] # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice:input(MENU)  # Hold the choice made by the user.
parts: list[str,str]
# When the program starts, read the file data into a list of lists (table)
try:
    file=open(FILE_NAME, "r")
    students=json.load(file)
except FileNotFoundError as e:
    print("File not found")
    file=open(FILE_NAME, "w")
    print(e, e.__doc__)
except json.decoder.JSONDecodeError as e:
    print("Json file issue")
    print(e, e.__doc__)
finally: file.close()


# Extract the data from the file
student_data = json.load(file)
student_first_name = student_row1["Firstname"]
student_last_name = student_row1["Lastname"]
course_name = student_row1["course"]
# Transform the data from the file
json.dump(student_row1,student_row2)
# Load it into our collection (list of lists)
for item in student_data:
 students.append(student_data)
 file.close()

# Present and Process the data
while (True):
# Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

# Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
     student_first_name = input("Enter the student's first name: ")
     student_last_name = input("Enter the student's last name: ")
     course_name = input("Please enter the name of the course: ")
     student_data = [student_first_name, student_last_name, course_name]
     students.append(student_row1)
     print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
     continue

# Present the current data
    elif menu_choice == "2":
     # Process the data to create and display a custom message
     print(student_row1)

     continue
# Save the data to a file
    elif menu_choice == "3":
        file = open(FILE_NAME, "w")
        json.dumps(students, file)
        continue

# Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
