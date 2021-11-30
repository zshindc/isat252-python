# delimeters with print function
print('One', end=' ')
print('Two', end=' ')
print('Three')

# sep delimeter
print()
print('One', 'Two', 'Three', sep='*')

# concentration, tabs, etc.
print('my name is \nTony')
print('my name is \t\tTony')
print('Tony' + 'Teate')


# This program demonstrates how a floating-point
# number can be formatted.
amount_due=5000.0
monthly_payment=amount_due/12
print('The monthly payment is', format(monthly_payment, '.2e'))

print(format(12345123524.6789, ',.2f'))
