# This program uses the for loop to read
# all of the values in the sales.txt file.


def main():
    # OPen the sales.txt file for reading
    sales_file = open('sales.txt', 'r')

    # create variable to hod total
    total = 0.0
    # Read all the lines from the file.
    for line in sales_file:
        # Convert line to a float.
        amount = float(line)
        total += amount
        count += 1
        # Format and display the amount.
        print(format(amount, '.2f'))

    # Close the file.
    sales_file.close()
    print('The total sales were:', format(total, '.2f'), 'dollars')
    print('There were {} sales today'.format(count))


# Call the main function.
main()
