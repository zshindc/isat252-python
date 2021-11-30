#MilesPerGallon Program
#Programmer: Zachary Shin
#Language: Python 3.9.x
#miles-per-gallon.py

#declare miles driven & gallons used
miles_driven=0.0
gallons_of_gas=0.0

#get driven miles & gallons used (input)
miles_driven=float(input('How many miles did you drive in your car? '))
gallons_of_gas=float(input('How many gallons of gas did you use in your car? '))

#calculate car's MPG (processing)
MPG=miles_driven/gallons_of_gas

#display MPG
print("Your car's MPG is", format(MPG,'.2f'), "miles per gallon.")
                     
