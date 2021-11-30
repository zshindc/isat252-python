# imports

# Zachary Shin

def compute_maximum(weekly_gas_average):
    maximum = max(weekly_gas_average)
    return maximum


def compute_minimum(weekly_gas_average):
    minimum = min(weekly_gas_average)
    return minimum


def compute_avg(weekly_gas_average):
    avg = sum(weekly_gas_average)/len(weekly_gas_average)
    return avg


def main():

    # Open the gas data file.
    infile = open('1994_Weekly_Gas_Averages.txt', 'r')

    # Read and process the file contents and store in a list (these are your y-values).
    weekly_gas_average = infile.readlines()
    weekly_gas_average.rstrip('\n')

    # Close the file.
    infile.close()

    # Print the list
    print(weekly_gas_average)

    # Call the function(s) to return the statistics
    
    compute_maximum(weekly_gas_average)
    compute_minimum(weekly_gas_average)
    compute_avg(weekly_gas_average)

    # Print the statistics
    print('The maximum value of all the values is :', maximum)
    print('The minimum value of all the values is :', minimum)
    print('The average value of all the values is :', avg)

    # Create a list containing the week numbers (to use as the x-values).

    # Build the graph.

    # Add a title.

    # Add labels to the axes.

    # Display and save the graph.


main()
