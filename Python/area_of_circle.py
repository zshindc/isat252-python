#Purpose of Program
#Programmer: Zachary Shin
#Language: Python 3.7.x
#area_of_circle.py

#create and initialize variables and constants
radius=0.0
area=0.0
PI=3.14

#input - get the radius of the circle
radius=float(input('What is the radius of the circle? '))

#process - compute the area of the circle
area=PI*radius**2

#output - display the result
print('The area of the circle is', area)
