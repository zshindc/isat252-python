#Quadratic Equation Program
#Programmer: Zachary Shin and 
#Language: Python 3.9.x
#quadratic.py
#program that computes the roots of a quadratic equation

#import the math module (your first import of prewritten code)
import math

#declare and initialize variables
a=0.0
b=0.0
c=0.0
discRoot=0.0
discrim=0.0
root1=0.0
root2=0.0
x=0.0
#message to users
print("The following program finds the solutions to a quadratic equation.")

#find inputs (coefficients) from users
a = float(input("\nPlease enter the coefficient (a): "))
b = float(input("\nPlease enter the coefficient (b): "))
c = float(input("\nPlease enter the coefficient (c): "))


#trap for bad input
if a == 0:
    print("The solution with given (a) coefficient doesn't present a possible solution.")
else:
    print("The solution is possible.")
    
#compute the discriminant
discrim=(4*a*c)-(b**2)


#checking if discriminant is positive, negative or zero and compute the roots
x=(-b/(2*a))
    
    
discRoot=math.sqrt(discrim)/(2*a)

#decision structure and processing

if discRoot == 0:
    print("The answer is," format(x, '.2f'),".")

elif discRoot > 0:
    discRoot =format(discRoot, '0.2f')
    root1 = str(x) + ' + ' str(discRoot)
    root2 = str(x) + ' - ' str(discRoot)
    print("The solutions are:", root1, " and ", root2)
    
elif discRoot < 0:
    discRoot =format(discRoot, '0.2f')
    root1 = str(x) + ' + ' + discRoot +'i'
    root2 = str(x) + ' - ' + discRoot +'i'
print("\nThe solutions are:", root1, " and ", root2)


