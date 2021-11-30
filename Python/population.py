#Program 3: Population 
#Programmer: Zachary Shin
#Language: Python 3.7.x
#population.py

#The program predicts the appromximate size of a population of organisms.

#textboxes that input starting number of organisms, avg daily population increase
#(as percentage), and days to multiply the organism.

organism_start = int(input("Starting number of organisms: "))
Avg_daily_increase = float(input("Average daily increase percentage: "))
days = int(input("Number of days to Multiply: "))

print("Day\tApproximate Population")

for days in range(1, 1 + days):
    if days == 1:
        appox_population = organism_start
    else:
        appox_population *= (1 + Avg_daily_increase/100)
    print(days, '\t', format(appox_population, '.4f'))
        
    





