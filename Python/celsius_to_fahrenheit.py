#Program 1: Celsius to Fahrenheit Table Program
#Programmer: Zachary Shin
#Language: Python 3.7.x
#celsius_to_fahrenheit.py

#this program displays a table of the Celsius temps 0-20
#and the Fahrenheit equivalents.

#initialize variables
F = 0.0
C = 0

#Print table headings
print('Celsius\tFahrenheit')

#print the Celsius temps: numbers 0 thru 20
for C in range(1,21):
    #given formula to convert Celsius to Fahrenheit
    F = (9/5)*C+32
    #print the numbers for Celsius and fahrenheit equivalents
    print(C, '\t', format(F, '.1f'))
    
    

