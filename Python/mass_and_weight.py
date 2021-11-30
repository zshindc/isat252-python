# MassandWeight program
#Programmer: Zachary Shin
#Language: Python 3.9.x
#mass_and_weight.py

#variables
mass=0.0
weight=0.0

#get mass (input)
mass=float(input("What is the object's mass in kg? ")

# calculate weight
weight = mass*9.8

#display the object's weight
print("The object's weight is", format(weight, '.2f'), "newtons.")
           
# determine weight
if weight >= 500:
    print("Object is too heavy.")
elif weight <= 100:
    print("Object is too light.")
else:
    print("Object is in an acceptable range.")

