# Program that displays average value of inputed file data 
# Programmer: Zachary Shin
# Language: Python 3.7.x
# lab07.py

def main():
    # Local variables
    file = None
    i = 0
    columnName = None
    count = 0
    sum = 0
    # input name of file
    while file == None:
        filename = input('Enter the filename LabpH.txt or Turbidity.txt' +\
                         ' you wish to open (not case sensitive): ')

        # decision structure to open one of two files or an invalid file
        if (filename.lower() == "labph.txt"):
            file = open("LabpH.txt", 'r')

        elif (filename.lower() == "turbidity.txt"):
            file = open("Turbidity.txt", 'r')

        else:
            print("Invalid file")

    # Process sum of values and count of numbers in file
    for line in file:

        try:
            if (i == 0):
                columnName = line.replace('\n', '').replace('\r', '')
                i += 1
            else:
                value = float(line.replace('\n', ''))
                sum += value
                count += 1
                
        # Errors in input        
        except ValueError:
            print("Invalid input found = " + line)
        except IOError:
            print('An error occurred trying to read the file.')
        except ValueError:
            print('Non-numeric data found in the file.')
        except Exception as e:
            print(e)
        except:
            print('An error occurred.')
            
    # Close the file
    file.close()
    
    # Calculate average value of file
    avg = sum / count

    # Output displays column title and average value
    print(columnName)
    print("Average: ", str(format(avg, '.2f')))
    print()
    # 2nd output displays a sentence telling what was measured and avg reading.
    print("The program measured " + \
          "the average reading for file " + filename + " in the column " + columnName + \
          " which is " + str(format(avg, '.2f')) +
        ".")


main()


