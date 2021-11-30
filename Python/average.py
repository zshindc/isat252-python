# accumulator

# average.py
# A program to average a set of numbers
# Illustrates counted loop with accumulator

# get number of iterations from user
n = int(input("How many numbers do you have? "))

# initialize and start loop
sum = 0.0
for i in range(n):
    x = float(input("Enter a number >> "))
    sum = sum + x
average=sum/n
print("\nThe average of the numbers is", average)
