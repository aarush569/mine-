# Write a Python program that calculates the total mark score of a student based on their marks in five
# subjects. The program should then determine the student's result based on their average marks and whether
# they have passed or failed in each subject.
# Follow these conditions for determining the result:
#
# Passing Marks: The passing mark for each subject is 40.
# Result Criteria:
# Distinction: Average marks of 75 or above.
# First Class: Average marks between 60 and 74.
# Second Class: Average marks between 50 and 59.
# Passed: Average marks between 40 and 49.
# Failed: If the student fails in any subject (i.e., scores below 40 in any subject).

a=float(input("enter the marks of a student in english:"))
b=float(input("enter the marks of a student in maths:"))
c=float(input("enter the marks of a student in physics:"))
d=float(input("enter the marks of a student in chemistry:"))
e=float(input("enter the marks of a student in biology:"))
average=((a+b+c+d+e)/5)
if average>100:
    print("it is not existing")
elif average>75 and average<100:
    print("disticntion")
elif average>60 and average<74:
    print("first class")
elif average>50 and average<59:
    print("second class")
elif average>40 and average<49:
    print("passed")
else:
    print("failed")