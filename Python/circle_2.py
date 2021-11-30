#Program computes the area of a circle through functions
#Programmer: Zachary Shin
#Language: Python 3.9.x
#circle_2.py

def main():
    # declare variables and constants
    radius = 0.0
    # get input
    radius = float(input('What is the radius of the circle? '))
    # call compute_are function and pass it the radius
    compute_area(radius)
    
def compute_area(radius):
    # declare variables and constants
    area = 0.0
    PI = 3.14
    # process - compute the area of the circle
    area = PI*radius**2
    # output - display the result
    print('The area of the circle is', format(area, '.2f'))

main()
