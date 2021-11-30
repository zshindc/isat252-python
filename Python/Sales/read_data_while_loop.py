# This program reads all of the values

def main():
    # Open the sales.txt file for reading.
    sales_file = open('sales.txt', 'r')

    # Read the first line from the file, but
    # don't convert to a number yet. We still
    # need to test for an empty string
    line = sales_file.readline()

    # As long as an empty string is not returned
    # from readline, continue processing.
    total = 0.0
    while line != '':
        # Convert line to a float
        amount = float(line)
        total += amount

        #Format and display the amount.
        print(format(amount, '.2f'))

        # REad the next line
        line = sales_file.readline()

    # Close the file.
    sales_file.close()
    print('total = ', total)

# Call the main function.
main()
