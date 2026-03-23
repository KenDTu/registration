"""
The main.py module defines the classes for each course to be registered. 

Class descriptions:
- Course
    - This class has the courseName, courseID, hmcCredits, schedule
"""

class Course:
    # A class attribute, shared by all instances
    species = "canine"

    # The __init__ method (constructor) initializes instance attributes
    def __init__(self):
        self.name = name  # Instance attribute for the dog's name
        self.age = age    # Instance attribute for the dog's age

    # A method (function inside the class)
    def bark(self):
        return f"{self.name} says woof!"

    # A special method to provide a user-friendly string representation
    def __str__(self):
        return f"{self.name} ({self.age})"

# Deserialization of the class data classData.json
# Construct each class object using data from the JSON



