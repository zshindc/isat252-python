#Program 2: Celsius to Fahrenheit Table Program
#Programmer: Zachary Shin
#Language: Python 3.7.x
#average_rainfall.py

# This program displays number of rainfall months, total inches of rainfall,
#and avg rainfall per month for entire period through a nested loop

#asks number of years
rainfall_years = int(input("Over how many years are you collecting data and \
calculating the average rainfall? "))
                                      
avg_rainfall = 0.0
rain_sum = 0
                     
#outer loop will iterate once for each year
for i in range(rainfall_years):
    #inner loop will iterate 12 times, 1 each month
    for j in range(12):
        #each iteration of inner loop asks user for inches of rainfall for that month
        rainfall = float(input("Enter rainfall for the month in inches: "))
        rain_sum = rain_sum + rainfall
                                      
#calculate avg rainfall per month for entire period                                      
avg_rainfall = rain_sum/(rainfall_years*12)


#display number of rainfall months
print()
print("There are", rainfall_years*12, "rainfall months.")
#display total inches of rainfall
print("There is a total of", format(rain_sum, '.2f'), "inches of rainfall.")
#display avg rainfall per month for entire period
print("The average rainfall per month for the entire period is", format(avg_rainfall, '.2f'),\
      "inches per month.")


                



