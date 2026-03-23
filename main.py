"""
The main.py module defines the classes for each course to be registered. 

Class descriptions:
- Course
    - This class has the name, courseID, schedule, creditHours
"""
import json

class Course:

    # The __init__ method (constructor) initializes instance attributes
    # Each parameterized constructor passes this 
    # {'name': 'Advanced Systems Engineering II', 'courseID': 'ENGR102 HM-01', 'schedule': {'Monday': '0935-1050', 'Wednesday': '0935-1050'}, 
    # 'creditHours': 3} in
    def __init__(self, data):
        self.name = data["name"]  
        self.courseID = data["courseID"]
        self.schedule = data["schedule"]    
        self.creditHours = data["creditHours"]      

# Open and load the JSON data
with open('classData.json', 'r') as file:
    data = json.load(file)
    classData = data["classes"] # some redudancy with the classes


# Deserialization of the class data classData.json
# Construct each class object using data from the JSON & append each object to classes

classes: list[Course] = []

# Append all course objects to a list of Courses
for course in classData:
    classes.append(Course(course)) 






# engineering: Course = Course({'name': 'Advanced Systems Engineering II', 'courseID': 'ENGR102 HM-01', 'schedule': {'Monday': '0935-1050', 'Wednesday': '0935-1050'}, 'creditHours': 3})

