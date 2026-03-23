# This python file just helps me develop practice with manipulating the data from the possibleClasses.json file

import json

# Open and load the JSON data
with open('classData.json', 'r') as file:
    data = json.load(file)

# 'data' is now a Python dictionary or list
# print(data)

class_list = data["classes"]

# print(class_list)

# for course in class_list:
#     name = course["name"]
#     course_id = course["courseID"]
#     schedule = course["schedule"]
#     credits = course["creditHours"]

#     print(name)
#     print(course_id)
#     print(schedule)
#     print(credits)

# data["classes"][0]["name"]
# data["classes"][i] returns the ith class object
# whilst the ["name"] on its right returns the member variable
first_course = data["classes"][0]["name"]
print(first_course)

# data["classes"][0]["schedule"]
# ["schedule"] on its right returns the member variable schedule
# ["Day"] returns the time period. This will produce a KeyError if the Day does not exist within the schedule
first_course = (data["classes"][0])["schedule"]["Wednesday"]
print(first_course)

