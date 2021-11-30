#Program computes the area and circumference
# of a circle
#Programmer: Zachary Shin
#Language: Python 3.6.x
#circle_3.py

#declare global variables and constants
PI = 3.14

def compute_area(radius):
    #declare variables and constants
    area = 0.0
    #process - compute the area of the circle
    area = PI*radius**2
    #return computed value back to main()
    return area

def compute_circumference(radius):
    #declare variables and constants
    circumference = 0.0
    #process - compute the circumference of the circle
    circumference = 2*PI*radius
    #return computed value back to main()
    return circumference

def main():
    #declare variables and constants
    radius = 0.0
    #input - get the radius
    radius = float(input('What is the radius of the circle in meters? '))
    #call the functions and display the returned values
    area = compute_area(radius)
    circumference = compute_circumference(radius)
    #output - display the results
    print('The area of the circle is', format(area, '.2f'), 'meters squared.')
    print('The circumference of the circle is', format(circumference, '.2f'), 'meters.')

main()
