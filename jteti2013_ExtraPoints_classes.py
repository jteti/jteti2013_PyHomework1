# Extra Points
# Create a class called Student that has the properties:
class Student:
    # Count variable set to 0
    studentCount = 0

    def __init__(self, name, age, birthmonth ):
        # name (holds student name)
        self.name = name
        # age (holds student age)
        self.age = age
        # birthmonth (holds students birthmonth)
        self.birthmonth = birthmonth
        # Upon each call to the class this variable increments
        Student.studentCount += 1

    # Function Displayname returns the student name
    def displayName(self):
        print("Student name: ", self.name)
    # Function DisplayBirthmonth returns the student birthmonth
    def displayBirthmonth(self):
        print("Birthmonth: ", self.age)
