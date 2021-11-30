# This program demonstrates an infinite loop

# Create a variable to control the loop.
keep_going = 'y'

#Warning! Infinite loop!
while keep_going =='y':
    # Get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

    # Calculate the comission.
    commission = sales*comm_rate

    # Display the commission
    print('The commission is $', \
          format(commission, ',.2f'), sep='')

    # See if the user wants to do another one.
    keep_going = input('Do you want to caluculate another'+ \
                       'commission (Enter y for yes): ')
    
