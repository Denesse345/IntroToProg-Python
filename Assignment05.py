# ------------------------------------------------------------------------------------------- #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   DGomez,5/26/24,Created Script
#   <Denesse Citlaly Gomez>,<5/26/24>, <Assignment 05>
# ------------------------------------------------------------------------------------------ #
import json

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
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {} # one row of student data
students: list = []  # a table of student data
# csv_data: str = '' # csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = '' # Holds combined string data in a json file
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

try:
    file = open(FILE_NAME, "r")
    students = json.load(file)

    file.close()

except Exception as e:
    print("Error opening file")
    print("Please check you have entered the correct json")
    print(e.__doc__)
finally:
    if file.closed == False:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Student First Name must be alphabetic")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Student Last Name must be alphabetic")
            course_name = input("Please enter the name of the course: ")
            student_data = {'first_name': student_first_name, 'last_name': student_last_name, 'course_name': course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)
        except Exception as e:
            print("Error with entered data")
            print(e.__doc__)
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:
            print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course_name']}")
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")

            json.dump(students, file)
            file.close()

            print("The following data was saved to a file!")
            for student in students:
                print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course_name']}")
        except Exception as e:
            if file.closed == False:
                file.close()
            print('Error saving data to file')
            print(e)
            print(e.__doc__)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
else:
    print("Only choose option 1, 2, or 3")

print("Program Ended")
