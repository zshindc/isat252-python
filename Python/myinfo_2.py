#getting input from the keyboard
# program: keyboard_input.py
# language: Python 3.9
# ISAT 252
# by Zachary shin

#Create variables initalize to their null values
name=''
age = 0
income = 0.0

# get input from keyboard for variables

name=input('What is your name? ')
age=int(input('What is your age? '))
income=float(input('What is your income? '))

print('My name is', name, 'and I am', age, 'years old.')
print('My major is ISAT')
print('My monthly income is', income, 'dollars')
print('I think "Python Programming" is fun!')

