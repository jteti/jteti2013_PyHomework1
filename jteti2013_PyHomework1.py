# 1. Print "Hello World"
print("Hello World \n")

# 2. Save your age to a variable called "age"
#declaring age. Must cast numeric to str
age = int('38')

# 3. Print "Hello World, I'm (age variable) today."
print("Hello World, I'm " + age + " today. \n")

# 4. Print "hello world" in all upper case using a python function to alter it
# Declaring string to variable hw
hw = 'hello world \n'
# Printing string in all upper case letters
print(hw.upper())

# 5. Save any decimal in a variable called a
a = 1.5

# 6. Cast a into an int and save it as b
b = int(a)

# 7. Cast a into a string and save it as c
c = str(a)

# 8. Print each variable and its type
print(a)
print(type(a), "\n")
print(b)
print(type(b), "\n")
print(c)
print(type(c), "\n")

# 9. Create a tuple of your favorite things to eat and print it
foods = ('Lasagna','Chicken Picata','Pizza')

# 10. Create a dictionary named 'classes' with the names of the classes
# you are taking as the keys and the professors names as the values
classes = {'Programming Languages ':'Dr. Huang', 'Formal Languages ':'Dr. Fernandez', 'Digital Image Processing ':'Dr. Marques'}

# 11. Print the dictionary and tuple
for k, v in classes.items():
    print(k,v)
print(foods)

# 12. Create a list called "whole" and put every number in it from 1 - 100
# Build empty list named whole
whole = []
# Use range function to do 1 to 100 counts
for i in range(1,101):
    whole.append(i)

print('\n')
# 13. Create 4 empty lists called 'div2', 'div3', 'div4', and 'div5'
div2 = []
div3 = []
div4 = []
div5 = []

# 14. Create a loop that examines each number from 1 to 100
# If divisible by 2, put in div2
for i in whole:
    if i % 2 == 0:
        div2.append(i)

# If divisible by 3, put in div3
for i in whole:
    if i % 3 == 0:
        div3.append(i)

# If divisible by 4, put in div4
for i in whole:
    if i % 4 == 0:
        div4.append(i)

# If divisible by 5, put in div5
for i in whole:
    if i % 5 == 0:
        div5.append(i)

# 15. Print all 5 of these lists
print("list whole = ", whole)
print("list div2 = ", div2)
print("list div3 = ", div3)
print("list div4 = ", div4)
print("list div5 = ", div5)

# 16. Create a new list called "divOver5"
divOver5 = []

# 17. Create a new loop that goes through each number 1 through 100 and appends it to
# divOver5 if it is NOT IN div2 or div3 or div4 or div5
for i in whole:
    if i not in div2 or i not in div3 or i not in div4 or i not in div5:
        divOver5.append(i)

# 18. Print divOver5
print("\n" "divOver5 = ", divOver5)

# 19. Create a function called exp3 that takes an int x, raises it to the third power
# and then returns a string that syas "x is divisible by 3"
x = 3
if x ** 3 % 3 == 0:
    print("x is divisible by 3")
# Test for not divisble by 3
x = 2
if x ** 3 % 3 != 0:
    print("x is not divisble by 3")

print("\n")

# 20. Iterate through the classes dictionary and print the keys
for k, v in classes.items():
    print(k)

print("\n")
# 21. Iterate through the classes dictionary and print the keys
for k, v in classes.items():
    print(v)

print("\n")


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

# Extra Points
import jteti2013_ExtraPoints_classes

# Create 3 students
# This would create first object of Student class
std1 = jteti2013_ExtraPoints_classes.Student("John", "38", "September")
# This would create second object of Student class
std2 = jteti2013_ExtraPoints_classes.Student("Albert", "129", "March")
# This would create third object of Student class
std3 = jteti2013_ExtraPoints_classes.Student("Alan", "103", "June")

# Call displayName() on student1
std1.displayName()

# Call displayBirthmonth() on student2
std2.displayBirthmonth()

# Print the student count
print("Total student count: %d" % jteti2013_ExtraPoints_classes.Student.studentCount)
